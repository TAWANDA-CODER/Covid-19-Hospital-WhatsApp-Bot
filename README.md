# Covid-19-Hospital-WhatsApp-Bot using Twilio
![COVID-19 WHATSApp bot](https://user-images.githubusercontent.com/74461990/175829929-59d270f4-6b94-4764-8eb8-4987c4fe8e4e.png)

Covid-19-Hospital-WhatsApp-Bot to check up on patients current health status using twilio

<h1>Requirements</h1>
<h3>Install Twilio Dependencies</h3>

wget -qO- https://twilio-cli-prod.s3.amazonaws.com/twilio_pub.asc \
  | sudo apt-key add -
sudo touch /etc/apt/sources.list.d/twilio.list
echo 'deb https://twilio-cli-prod.s3.amazonaws.com/apt/ /' \
  | sudo tee /etc/apt/sources.list.d/twilio.list
sudo apt update
sudo apt install -y twilio

<h3>Install Python Apscheduler</h3>   

$ pip install apscheduler
