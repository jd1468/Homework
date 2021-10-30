import threading
import time


class Philosopher(threading.Thread):
	running = True

	def __init__(self, index, left_fork, right_fork):
		threading.Thread.__init__(self)
		self.index = index
		self.left_fork = left_fork
		self.right_fork = right_fork

	def run(self):
		while self.running:
			time.sleep(30)
			print('Philosopher %s is hungry.' % self.index)
			self.eat()

	def eat(self):
		fork1, fork2 = self.left_fork, self.right_fork
		while self.running:
			fork1.acquire()
			locked = fork2.acquire(False)
			if locked:
				break
			fork1.release()
			print(f'Philosopher {self.index} swaps forks.')
			fork1, fork2 = fork2, fork1
		else:
			return
		self.eating_process()

		fork2.release()
		fork1.release()

	def eating_process(self):
		print(f'Philosopher {self.index} starts eating. ')
		time.sleep(30)
		print(f'Philosopher {self.index} finishes eating and leaves to think.')


def main():
	forks = [threading.Semaphore() for _ in range(5)]

	philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

	Philosopher.running = True
	for i in philosophers:
		i.start()
	time.sleep(100)
	Philosopher.running = False
	print('Done')


if __name__ == "__main__":
	main()
