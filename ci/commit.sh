echo "\nSetting up Git"
if [ -z "`git config --get --global credential.helper`" ]; then
  echo "\nset up credential.helper"
  git config credential.helper "store --file=.git/credentials"
  echo "\nhttps://monkeyboy2805:@github.com" > .git/credentials 2>/dev/null
fi
if [ -z "`git config --get --global user.email`" ]; then
  echo "\nset up user.email"
  git config --global user.email "monkeyboy2805@gmail.com"
fi
if [ -z "`git config --get --global user.name`" ]; then
  echo "\nset up user.name"
  git config --global user.name "Monkeyboy2805"
fi
echo "\nCreating commit"
git checkout ci_test_bot
git checkout -b ci_test_bot_AA
git commit -m "Try to do SOMETHING"
COMMIT_EXIT_STATUS=$?
if [ $COMMIT_EXIT_STATUS -gt 0 ]; then
  notice "Nothing to commit"
  exit $EXIT_NOTHING_TO_COMMIT
fi
notice "Pushing commit"
if [ -z $GITHUB_OAUTH_TOKEN ]; then
  warn '$GITHUB_OAUTH_TOKEN not set'
  exit 1
fi
git push origin ci_test_bot_AA
then
