# pytest-web

(Below steps are based on WinOs)

## 1. Install Node.js, Java, Python.

## 2. Install pip packages for your project.

```commandline
pip install -r requirements.txt
```

## 3. Install Appium.

```commandline
npm install -g appium
```

## 4. Install uiautomator2 driver.

```commandline
npm install -g appium-uiautomator2-driver
```

## 5. Install Android SDK(Usually you can install it by installing Android Studio).

https://developer.android.com/studio

## 6. Configure system environment variables on your PC:

* ANDROID_HOME
```commandline
<your installation directory of Android Studio>\Android\Sdk
```

* ANDROID_SDK_ROOT
```commandline
<your installation directory of Android Studio>\Android\Sdk
```

## 7. Update PATH on your PC.

%ANDROID_HOME%\platform-tools

## 8. Start appium server.

```commandline
appium
```

## 9. Run your automation script, like:

```commandline
python runner.py - run

python runner.py - generate_report

python runner.py - open_report

python runner.py - generate_report - open_report

python runner.py - run - generate_report - open_report

python runner.py - run --keyword=test_demo

python runner.py - run --mark=P0

python runner.py - run --keyword=test_demo --mark=P0

python runner.py - run --case_files=tests\feature_a\test_android_demo.py

python runner.py - run --last_failed=True

python runner.py - run --concurrency=2

python runner.py - run --maxfail=2

python runner.py - run --failed_first

python runner.py - run --ignore=tests\feature_a\test_android_demo.py
```

## 10. If you got errors like below, then you may need to restart your PC.

```commandline
UnknownError: An unknown server-side error occurred while processing the command. Original error: Neither ANDROID_HOME nor ANDROID_SDK_ROOT environment variable was exported.
```