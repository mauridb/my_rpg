from model.system_abstract_factory import DeDSystem, get_factory


def main():
	for index in range(1):
		ded = DeDSystem(get_factory())
		ded.show_object_factory()


if __name__ == '__main__':
	main()
