
#include <time.h>
#include <stdio.h>
#include <iostream>
#include <math.h>
#include "EdcCloudClient.h"
#include "i2c-host.h"

// >>>>>> Set these variables according to your Cloud user account

#define I2C_DEV_NAME  		"/dev/i2c-1"
#define TEST_CLIENT_ID		"wilsmagicclient"		// Unique Client ID of this client device
#define TEST_ASSET_ID		"wilsmagicasset"		// Unique Asset ID of this client device

// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#define	DATA_SEMANTIC_TOPIC		"nativeclient/data"		// default publish topic
#define PUBLISH_PERIOD		10000			// time between published messages, in milliseconds
#define	MAX_PUBLISH		10			// number of times to publish
#define LATITUDE			46.369079			// default (simulated) GPS position
#define LONGITUDE			13.076729
#define ALTITUDE			320.0
#define PUBLISH_TIMEOUT		50000L			

#define DISPLAY_TX_MSG_PAYLOAD	
#define DISPLAY_RX_MSG_PAYLOAD	


bool displayPayload (EdcPayload * payload)
{
	if (payload == 0)
		return false;

	if (payload->has_timestamp())
		printf ("  timestamp: %lld\n", payload->timestamp());

	if (payload->has_position()) {

		const EdcPayload_EdcPosition position = payload->position();

		printf ("  position latitude: %f\n", position.latitude());
		printf ("  position longitude: %f\n", position.longitude());

		if (position.has_altitude())
			printf ("  position altitude: %f\n", position.altitude());
	
		if (position.has_precision())
			printf ("  position precision: %f\n", position.precision());

		if (position.has_heading())
			printf ("  position heading: %f\n", position.heading());

		if (position.has_speed())
			printf ("  position speed: %f\n", position.speed());

		if (position.has_timestamp())
			printf ("  position timestamp: %lld\n", position.timestamp());

		if (position.has_satellites())
			printf ("  position satellites: %d\n", position.satellites());

		if (position.has_status())
			printf ("  position status: %d\n", position.status());
	}

	for (int i=0; i<payload->metric_size(); i++) {

		EdcPayload_EdcMetric metrictmp = payload->metric(i);

		printf ("  metric #%d name: %s\n", i, metrictmp.name().c_str());
		printf ("  metric #%d type: %d\n", i, metrictmp.type());

		if (metrictmp.has_double_value())
			printf ("  metric #%d double_value: %f\n", i, metrictmp.double_value());

		if (metrictmp.has_float_value())
				printf ("  metric #%d float_value: %f\n", i, metrictmp.float_value());

		if (metrictmp.has_long_value())
			printf ("  metric #%d long_value: %lld\n", i, metrictmp.long_value());

		if (metrictmp.has_int_value())
			printf ("  metric #%d int_value: %d\n", i, metrictmp.int_value());

		if (metrictmp.has_bool_value())
			printf ("  metric #%d bool_value: %d\n", i, metrictmp.bool_value());

		if (metrictmp.has_string_value())
			printf ("  metric #%d string_value: %s\n", i, metrictmp.string_value().c_str());

		if (metrictmp.has_bytes_value()) {
			printf ("  metric #%d bytes_value:", i);
			
			for (int j=0; j<(int)(metrictmp.bytes_value().length()); j++)
				printf (" 0x%02x", metrictmp.bytes_value().data()[j]);

			printf ("\n");
		}
	}
	
	if (payload->has_body()) {

		printf ("  body:");
			
		for (int i=0; i<(int)(payload->body().length()); i++)
			printf (" 0x%02x", payload->body().data()[i]);

		printf ("\n");
	}

	return true;
}

EdcPayload * createPayload(int i2cConnection, bmp085_calib_data * calibration) {
	EdcPayload  * edcPayload = new EdcPayload();
	EdcPayload_EdcMetric * metric;

	enable_pressure(i2cConnection, calibration);

	metric = edcPayload->add_metric();
	metric->set_name("Temperature");
	metric->set_type(EdcPayload_EdcMetric_ValueType_FLOAT);
	float tempValue = readTemprature(i2cConnection, calibration);
	cout << "temp: " << tempValue << endl;
	metric->set_float_value(tempValue);

	enable_accel(i2cConnection);

	metric = edcPayload->add_metric();
	metric->set_name("X");
	metric->set_type(EdcPayload_EdcMetric_ValueType_INT32);
	metric->set_int_value(readX(i2cConnection)); // TODO: GO AND GET THE REAL DATA

	metric = edcPayload->add_metric();
	metric->set_name("Y");
	metric->set_type(EdcPayload_EdcMetric_ValueType_INT32);
	metric->set_int_value(readY(i2cConnection)); // TODO: GO AND GET THE REAL DATA

	metric = edcPayload->add_metric();
	metric->set_name("Z");
	metric->set_type(EdcPayload_EdcMetric_ValueType_INT32);
	metric->set_int_value(readZ(i2cConnection)); // TODO: GO AND GET THE REAL DATA


	// TODO: get actual GPS DATA
	EdcPayload_EdcPosition * position = edcPayload->mutable_position();

	//randomly vary the position
	position->set_longitude(LONGITUDE + rand() - 0.5);
	position->set_latitude(LATITUDE + rand() - 0.5);
	position->set_altitude(296);
	position->set_heading(2);
	position->set_precision(10);
	position->set_speed(60);
	position->set_satellites(3);
	position->set_status(1);

	time_t capturedOn;
	time(&capturedOn);

	position->set_timestamp(1000*capturedOn);

	edcPayload->set_timestamp(1000*capturedOn);

	return edcPayload;
}


//callback for message arrived
int EdcCloudClientMessageArrived(string topic, EdcPayload * payload){
	static int rxMsgCount = 0;
	rxMsgCount ++;

	printf("Message #%d arrived: topic=%s\n", rxMsgCount, topic.c_str());
	
	if (payload != 0){
		displayPayload(payload);
	}

	return 0;
}


//callback for message delivered
int EdcCloudClientMessageDelivered(){
	printf("message delivered\n");
	return 0;
}

//callback for connection lost
int EdcCloudClientConnectionLost(char * cause){
	printf("Connection lost\n");
	return 0;
}


int shutdown(EdcCloudClient * edcCloudClient) {
	int rc = edcCloudClient->stopSession();
	
	if (rc != EDCCLIENT_SUCCESS){
		printf("stopSession with error code %d", rc);
	}

	edcCloudClient->terminate();

	return rc;
}

int main(int argc, char ** argv) {

	if(argc < 5) {
		printf("error: missing broker url or account name or user name or password on commandline\n");
	}
	string url = argv[1];
	string account = argv[2];
	string username = argv[3];
	string password = argv[4];

	//the client instance
	EdcCloudClient edcCloudClient;
	
	// the i2c file
	const char * devName = I2C_DEV_NAME;
	int i2cConnection = connect_accel(devName);
	bmp085_calib_data calibration;

	int rc = EDCCLIENT_SUCCESS;
	string pubTSemanticTopic = DATA_SEMANTIC_TOPIC;
	string accountSemanticTopics = "#";
	string accountControlTopics = "#";

	cout << "url: " << url << " account: " << account << " user: " << username << endl; 

	EdcConfiguration conf;    
	conf.setAccountName(account);
	conf.setBrokerUrl(url);
	conf.setClientId(TEST_CLIENT_ID);
	conf.setDefaultAssetId(TEST_ASSET_ID);
	conf.setUsername(username);
	conf.setPassword(password);
	
	//Create device profile and set its properties
	EdcDeviceProfile prof;
	prof.setDisplayName(TEST_ASSET_ID);
	prof.setModelName("Native EDC Client");

	//set GPS position in device profile - this is sent only once, with the birth certificate
	prof.setLongitude(LONGITUDE);
	prof.setLatitude(LATITUDE);
	prof.setAltitude(ALTITUDE);

	//Create cloud client instance
	edcCloudClient = EdcCloudClient(&conf, &prof, 
		EdcCloudClientMessageArrived, 
		EdcCloudClientMessageDelivered,
		//Don't pass a connection lost callback
		//so the client will reconnect automatically
		0);

	rc = edcCloudClient.startSession();
	if ( rc != EDCCLIENT_SUCCESS) {
		printf("error starting session %d\n", rc);

		switch (rc)
		{
			// MQTT client errors (<0):
			case MQTTCLIENT_FAILURE:
				printf ("MQTT client, generic operation failure\n");
				break;
			case MQTTCLIENT_PERSISTENCE_ERROR:
				printf ("MQTT client, persistence error\n");
				break;
			case MQTTCLIENT_DISCONNECTED:
				printf ("MQTT client disconnected\n");
				break;
			case MQTTCLIENT_MAX_MESSAGES_INFLIGHT:
				printf ("MQTT client, maximum number of in-flight messages has been reached\n");
				break;
			case MQTTCLIENT_BAD_UTF8_STRING:
				printf ("MQTT client, invalid UTF-8 string\n");
				break;
			case MQTTCLIENT_NULL_PARAMETER:
				printf ("MQTT client, NULL parameter not allowed\n");
				break;
			case MQTTCLIENT_TOPICNAME_TRUNCATED:
				printf ("MQTT client, topic name truncated\n");
				break;
			case MQTTCLIENT_BAD_STRUCTURE:
				printf ("MQTT client, invalid structure\n");
			break;
		}	
		edcCloudClient.terminate();
		return rc;	
	}

	int qoss = 1;

	EdcPayload * payload = createPayload(i2cConnection, &calibration);
	rc = edcCloudClient.publish(pubTSemanticTopic, payload, qoss, false, PUBLISH_TIMEOUT);
	
	if (rc != EDCCLIENT_SUCCESS) {
		printf("Publish failed with error code %d\r\n", rc);
		delete payload;
		return shutdown(&edcCloudClient);
	}

	return shutdown(&edcCloudClient);

} 

