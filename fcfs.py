#!/usr/bin/env python3

class job:
    pid = 0

    arrivalTime = 0
    burstTime = 0

    waitingTime = 0
    completionTime = 0
    turnaroundTime = 0

    def input(self):
        print("Enter arrival time, burst time for pid ", pid, ": ")
        arrivalTime = int(input())
        burstTime = int(input())

JOBQUEUE = []

print("Number of jobs:")
a = int(input())

for i in range(a):
    a = job()
    a.input()
    JOBQUEUE.append(a)

for job in JOBQUEUE:
    time = 0
    print("PID\tBurstT\tArrivalT\tWaitingT\tCompletionT\tTurnaroundT")
    print("{}\t{}\t{}\t{}\t{}\t{}".format(job.pid, job.burstTime, job.arrivalTime, job.waitingTime, job.completionTime, job.turnaroundTime))
