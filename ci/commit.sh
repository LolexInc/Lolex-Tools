#!/bin/sh
git config --global user.email "monkeyboy2805@gmail.com"
git config --global user.name "monkeyboy2805"
git config --global user.token $token
git checkout ci_test_bot
git add *
git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
git push origin ci_test_bot
