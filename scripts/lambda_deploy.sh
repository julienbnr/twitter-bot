echo "Compress files for deploying on aws..."
zip -x LICENSE README.md /build* /.idea* /__pycache__* /.git* .DS_Store .gitignore -r lambda_deploy.zip .
echo "Process complete !"
