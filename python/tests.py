import unittest
import time

class Timer(object):
    
    def __init__(self, exercises, times, set_count):
        self.time = times
        self.data = exercises
        self.sets = set_count
        self.start_point = 0
        if self.sets < 1:
            self.sets = 1
        if self.time[1] < 20:
            self.time[1] = 20.0
        if self.time[0] < 10:
            self.time[0] = 10.0

           

    def get_current_exercises(self):
        if len(self.data) < 2:
            return [self.data[0], self.data[0]]

        if len(self.data) == self.start_point + 1:
            self.start_point = 0
            return [self.data[-1], self.data[0]]
        
        result = self.data[self.start_point:self.start_point + 2]
        self.start_point += 1
        return result

    def get_break_time_limit(self):
        return float(self.time[0])

    def get_exercise_time_limit(self):
        return float(self.time[1])

    def get_number_of_sets(self):
        return self.sets

    def display(self, p1, p2):
        for s in range(self.get_number_of_sets()):
            for ex in self.data:
                cur = self.get_current_exercises()
                print("Break! Up Next:")
                print(p1+": "+ cur[0])
                print(p2+": "+ cur[1])
                time.sleep(self.get_break_time_limit())
                print("Start Exercising")
                print(p1+": "+ cur[0])
                print(p2+": "+ cur[1])
                time.sleep(self.get_exercise_time_limit())
        return "Great Workout"              

class TimerTests(unittest.TestCase):

    def test_gets_first_2_exercises(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60] , 2)
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())

    def test_gets_next_2_exercises(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], 2)
        timer.get_current_exercises()
        self.assertEqual(['Pull Ups', 'Burpees'], timer.get_current_exercises())

    def test_gets_limited_exercises(self):
        timer = Timer(['Push Ups'],[10,60], 2)
        timer.get_current_exercises()
        self.assertEqual(['Push Ups', 'Push Ups'], timer.get_current_exercises())
        self.assertEqual(['Push Ups', 'Push Ups'], timer.get_current_exercises())

    def test_does_not_go_past_length(self):
        timer = Timer(['Push Ups', 'Pull Ups'],[10,60], 2)
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Push Ups'], timer.get_current_exercises())

    def test_resets_start_point_when_rollover(self):
        timer = Timer(['Push Ups', 'Pull Ups'],[10,60], 2)
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Push Ups'], timer.get_current_exercises())
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())

    def test_resets_start_point_when_rollover(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], 2)
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Burpees'], timer.get_current_exercises())
        self.assertEqual(['Burpees', 'Push Ups'], timer.get_current_exercises())
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())

    def test_gets_break_time(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], 2)
        self.assertEqual(10, timer.get_break_time_limit())

    def test_short_break_time(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[-7,60], 2)
        self.assertEqual(10, timer.get_break_time_limit())

    def test_gets_exercise_time(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], 2)
        self.assertEqual(60, timer.get_exercise_time_limit())

    def test_short_exercise_time(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,10], 2)
        self.assertEqual(20, timer.get_exercise_time_limit())

    def test_gets_sets(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], 2)
        self.assertEqual(2, timer.get_number_of_sets())

    def test_short_sets(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'],[10,60], -1)
        self.assertEqual(1, timer.get_number_of_sets())
   
    
if __name__ == '__main__':
    unittest.main(exit=False)

def main():
    print("Hello and welcome to your workout session")
    person1 = input("Name of person 1: ")
    person2 = input("Name of person 2: ")
    exercises = input("Please list desired workouts: ")
    exercises = exercises.split(',')
    times = [0.0,0.0]
    try:
       times[0] = float(input("Rest time: "))
    except ValueError:
       print("Invalid Value Type. Rest time is set to 10 sec")
       times[0] = 10.0
    try:
       times[1] = float(input("Exercise time: "))
    except ValueError:
       print("Invalid Value Type. Exercise time is set to 20 sec")
       times[1] = 20.0
    try:
        sets = int(input("Number of sets: "))
    except ValueError:
        print("Invalid Value Type. Number of sets is set to 2")
        sets = 2
    timer = Timer(exercises,times,sets)
    print("Your workout will begin in " + str(timer.get_break_time_limit())+  " seconds, Good Luck!")
    print(timer.display(person1,person2))
    
    
            
    
    

main()
