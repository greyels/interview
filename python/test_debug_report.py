import random as r

def debug_time(mins):
    account_time = r.randint(0, mins)
    scenario_time = r.randint(0, mins - account_time)
    pre_review_time = mins - account_time - scenario_time
    print(f'Test debug. Account -> {account_time}m')
    print(f'Test debug. Scenario -> {scenario_time}m')
    print(f'Test debug. Pre-review -> {pre_review_time}m')

debug_time(90)

