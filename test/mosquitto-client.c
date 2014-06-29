/**  Pi In The Sky MQTT Client
 *   Catapult Satellite Applications Inventorthon 2014
 */

#include <stdio.h>
#include <mosquitto.h>


#define MESSAGE_COUNT 10L
#define MESSAGE_SIZE 1024L



/* Call on connecting to a MQTT server */
void pie_connect_callback(void* mosq, int result)
{
	if(!result){
		fprintf(stderr, "Connected\n");
	}else{
		fprintf(stderr, "Connect failed\n");
	}
}



void pie_publish_callback(void *mosq, uint16_t mid)
{
}




int main(int argc, char *argv[])
{
	char* clientid = "RBP1";
	char *host = "localhost";
	int port = 1883;
	int keepalive = 60;
	bool clean_session = false;
	struct mosquitto *mosq = NULL;
	int count = 0;

	mosquitto_lib_init();
	mosq = mosquitto_new(clientid, NULL);
	if(!mosq){
		fprintf(stderr, "Error: Out of memory.\n");
		return 1;
	}

	mosquitto_connect_callback_set(mosq, pie_connect_callback);
	//mosquitto_publish_callback_set(mosq, pie_publish_callback);


	if(mosquitto_connect(mosq, host, port, keepalive, clean_session)){
		fprintf(stderr, "Unable to connect.\n");
		return 1;
	}

	

	uint8_t payload[] = "8.10\n";
	int ret;

	while(!mosquitto_loop(mosq, 1000)){
		if(count < MESSAGE_COUNT){
			if((ret = mosquitto_publish(mosq, NULL, "Temperature", sizeof(payload), payload, 0, false)) == MOSQ_ERR_SUCCESS){
				fprintf(stderr, "Message %d sent\n", count);
				count++;
			}
			else{
				fprintf(stderr, "Message %d not sent: error %d\n", count, ret);
			}
		}
		else{
			mosquitto_disconnect(mosq);
		}
	}

	mosquitto_destroy(mosq);
	mosquitto_lib_cleanup();
	return 0;
}
