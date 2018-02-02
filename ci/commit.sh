#!/bin/sh

setup_git() {
  git config --global user.email "monkeyboy2805@gmail.com"
  git config --global user.name "monkeyboy2805"
}

commit_website_files() {
  git checkout ci_test_bot
  git add *
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push origin ci_test_bot
}

setup_git
commit_website_files
upload_files
