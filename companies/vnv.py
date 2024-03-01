import copy
import itertools

import requests


class TinyStories:
    """Iterator over tiny stories."""

    def __init__(self):
        self.__current_ix = None

        text = requests.get(
            "https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt").text
        self.tiny_stories = [x.strip() for x in text.split("<|endoftext|>")]

    def __len__(self):
        return len(self.tiny_stories)

    def __iter__(self):
        self.__current_ix = 0

        return self

    def __next__(self):
        if self.__current_ix >= len(self):
            raise StopIteration

        v = self.tiny_stories[self.__current_ix]
        self.__current_ix += 1
        return v


# MapReduce framework
Map = lambda: map
FlatMap = lambda: itertools.chain.from_iterable
GroupBy = lambda k: lambda it: itertools.groupby(it, key=k)
SortBy = lambda k: lambda it: sorted(it, key=k)
Execute = lambda: list


def tokenizer(doc):
    return doc.split(' ')


def sum_per_word(key__value):
    key, value = key__value
    return key, sum((x[1] for x in key__value[1]))


# source = (s for i, s in enumerate(TinyStories()) if i < len(TinyStories()))
source = TinyStories()

tokens_stream = Map()(tokenizer, source)
token_stream = FlatMap()(tokens_stream)
token_count_stream = Map()(lambda word: (word, 1), token_stream)
sorted_token_count_stream = SortBy(lambda key__value: key__value[0])(token_count_stream)
grouped_token_count_stream = GroupBy(lambda key__value: key__value[0])(sorted_token_count_stream)
pipeline = Map()(sum_per_word, grouped_token_count_stream)

# _ = Execute()(Map()(print, pipeline))


# Implement TopK/BottomK
import heapq
import time


class TopK:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def __call__(self, pipeline):
        for word, count in pipeline:
            if len(self.heap) == self.k:
                heapq.heappushpop(self.heap, (count, word))
            else:
                heapq.heappush(self.heap, (count, word))
        return [(word, count) for count, word in self.heap]


class BottomK:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def __call__(self, pipeline):
        for word, count in pipeline:
            count = -count
            if len(self.heap) == self.k:
                heapq.heappushpop(self.heap, (count, word))
            else:
                heapq.heappush(self.heap, (count, word))
        return [(word, -count) for count, word in self.heap]


pipelineTopK = copy.deepcopy(pipeline)
pipelineNlargest = copy.deepcopy(pipeline)
pipelineSorted = copy.deepcopy(pipeline)

start = time.time()
print(TopK(k=10)(pipelineTopK))
# _ = Execute()(Map()(print, BottomK(k=10)(pipeline)))
print(f"TopK -> {time.time() - start}")

start = time.time()
print(heapq.nlargest(n=10, iterable=pipelineNlargest, key=lambda elem: elem[1]))
print(f"nlargest -> {time.time() - start}")

start = time.time()
print(sorted(pipelineSorted, key=lambda elem: elem[1], reverse=True)[:10])
print(f"sorted -> {time.time() - start}")

# TopK -> 1.2101075649261475
# nlargest -> 1.3210186958312988
# sorted -> 1.6386902332305908

# TopK -> 1.479996681213379
# nlargest -> 1.5038385391235352
# sorted -> 1.6230087280273438

# TopK -> 1.2190568447113037
# nlargest -> 1.2172846794128418
# sorted -> 1.8762545585632324

# TopK -> 1.2250456809997559
# nlargest -> 1.2089030742645264
# sorted -> 1.628849983215332

# TopK -> 1.2458469867706299
# nlargest -> 1.2808418273925781
# sorted -> 1.6282627582550049
