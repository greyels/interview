# Coding Challenge

Load the ship. 

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked boxes, but because the needed supplies are buried under many other boxes, the boxes need to be rearranged.

The ship has a giant cargo crane capable of moving boxes between stacks. To ensure none of the boxes get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the boxes are rearranged, the desired boxes will be at the top of each stack.

The expedition members don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which box will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of boxes and the rearrangement procedure (your puzzle input). For example:

Example: 

Starting configuration: 
```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
```

Plan: 

```
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

In this example, there are three stacks of boxes. Stack 1 contains two boxes: box Z is on the bottom, and box N is on top. Stack 2 contains three boxes; from bottom to top, they are boxes M, C, and D. Finally, stack 3 contains a single box, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of boxes is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one box is moved from stack 2 to stack 1, resulting in this configuration:

```
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
```

In the second step, three boxes are moved from stack 1 to stack 3. boxes are moved one at a time, so the first box to be moved (D) ends up below the second and third boxes:

```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
```

Then, both boxes are moved from stack 2 to stack 1. Again, because boxes are moved one at a time, box C ends up below box M:

```
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
```

Finally, one box is moved from stack 1 to stack 2:

```
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
```

The expedition members just need to know which box will end up on top of each stack; in this example, the top boxes are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the expedition members the message CMZ.

After the rearrangement procedure completes, what box ends up on top of each stack?


