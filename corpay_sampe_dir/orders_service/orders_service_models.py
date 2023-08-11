from rest_framework import serializers

class InstructSerializer(serializers.Serializer):


request_body_sample = {
    "orders": [ 
        {
        "ordNum": "10041836",
		"amount" : 100
        }
	],	
        "payments": [
           {
                "beneficiaryId": "testtestv5",
				"amount": 100,
				"currency": "INR",
				"method": "W",
                "purposeOfPayment":"fxvx",
				"remitterId": "00801OSCXZATTZNAZNC2"

            }
		],
        "settlements":[
			{
			    "accountId":"INCOMING-TEST-USD" ,
                "method":"W",
                "currency":"USD",
                "purpose" : "Spot"
	        }  
				
			    
		]	
    
}

