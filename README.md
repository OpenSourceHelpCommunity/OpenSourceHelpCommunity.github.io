# OpenSourceHelpCommunity.github.io
Website [WIP]


This is using Django(1.7.6) and bootstrap. [How it looks currently?](https://gyazo.com/8395caa42290fb5a7d32d6b75c07ff53).
Feel free to suggest a better design.

## To run this in your local

1. Clone this repository using
	```
	git clone git@github.com:OpenSourceHelpCommunity/OpenSourceHelpCommunity.github.io.git
	```

2. Go inside main Django app
	```
	cd oshc
	```

3. Syncdb

	```
	python manage.py syncdb
	```

4. Change path to static files in settings.py

	Right now this file is having path of my local. Just change the machine's username to your own.

	```
	STATICFILES_DIRS =  ()
	```
4. Run the app
	```
	python manage.py runserver
	```


Feel free to raise and fix issues.
For any questions, join #oshc-dev on Slack.

Note : All design related tasks have reward associated with them.

