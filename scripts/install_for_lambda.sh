mkdir -p build/python/lib/python3.8/site-packages
pip3 install requests tweepy discord-webhook -t build/python/lib/python3.8/site-packages
cd build
zip -r packages.zip .
