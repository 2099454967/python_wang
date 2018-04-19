import time
def play_game():
	for i in range(10):
		print('玩吃鸡,哒哒哒')
		time.sleep(1)
	print('你全家都来来')
	result = kill()
	if result == '削死了':
		print('挂了')
	else:
		print('死了')
def kill():
	print('一顿削')
	return '削惨了'
play_game()
kill()
