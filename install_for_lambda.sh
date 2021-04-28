mkdir -p build/python/lib/python3.8/site-packages
pip3 install requests tweepy -t build/python/lib/python3.8/site-packages
cd build
zip -r deploy.zip .
