const Age = require('./heartbeat-age.js');
const Client = require('azure-iot-device').Client;
const Message = require('azure-iot-device').Message;
const Protocol = require('azure-iot-device-mqtt').Mqtt;

let age = new Age()

function beat(idade = 5) {
    const error = Math.random() <= 0.05
    if (error) {
        return null
    }

    const outlier = Math.random() <= 0.1
    if (outlier) {
        return 999
    }

    if (idade < 2) {
        return age.idadeMenor2Anos()
    } else if (idade >= 2 || idade < 4) {
        return age.idadeEntre2AnosE4Anos()
    } else if (idade >= 4 || idade < 6) {
        return age.idadeEntre4AnosE6Anos()
    } else if (idade >= 6 || idade < 12) {
        return age.idadeEntre6AnosE12Anos()
    } else {
        return age.idadeEntre12AnosE17Anos()
    }

}

function sweat() {
    const error = Math.random() <= 0.05
    if (error) {
        return null
    }

    const outlier = Math.random() <= 0.1
    if (outlier) {
        return 999
    }

    const baixoSuor = Math.random() <= 0.2
    if (baixoSuor) {
        return 0.15 - parseInt(Math.random() * 0.15)
    }

    const excessoSuor = Math.random() <= 0.2
    if (excessoSuor) {
        return 1.5 + parseInt(Math.random() * 0.5)
    }

    return 0.70 + parseInt(Math.random() * 2)

}

var result;
var bateria = 100;
function battery() {
    result = bateria - 0.005
    bateria = result
    return result.toFixed(3)
}

function parseBeat(beat, sweat, battery) {
    const msg = new Message(
        // `{"beat": ${beat}, "sweat": ${sweat}, "battery": ${battery}}`
        // `{"payload": "${beat},${sweat},${battery}"}`
        `{"Beat": ${beat}, "Sweat": ${sweat}, "Battery": ${battery}}`
    )

    msg.ContentEncoding = "utf-8";
    msg.ContentType = "application/json";
    msg.properties.add("sensorAutism", "IOTLog");

    if (beat >= 115) {
        msg.properties.add("crise", "yes")
    } else {
        msg.properties.add("crise", "no")
    }
    
    if (sweat >= 1.7) {
        msg.properties.add("crise", "yes")
    } else {
        msg.properties.add("crise", "no")
    }

    return msg
}

function sendMessage(){
    bpm = beat()
    suor = sweat()
    bateria = battery()
    msg = parseBeat(bpm, suor, bateria)
    console.log(msg)

    client.sendEvent(msg, (err) => {
        if(err) {
            console.error("Failed to send events")
        }else{
            console.log("Message sent")
        }
    })
}

function start(request, response) {
    response.send(200, "Sensor started", (err) => {
        if (err) {
            console.error("Failed to start: "+err.message)
        }
    })
}

function stop(request, response) {
    response.send(200, "Sensor stopped", (err) => {
        if(err){
            console.error("Failed to stop: "+err.message)
        }
    })
}

function receiveMessageCallback(msg) {
    const message = msg.getData().toString("utf-8")
    client.complete(msg, () => {
        console.log("Message received: "+message)
    })
}
const connectionString = "HostName=jennifer02201043.azure-devices.net;DeviceId=autism-pi;SharedAccessKey=BY5ieMyp/oBtexxNPvFjrFuuBLdsz+04qeWHkVXcnv8= "
const client = Client.fromConnectionString(connectionString, Protocol);

client.open(function (err) {
    if (err) {
        console.error(' Connect error: ' + err.message)
    }

    client.onDeviceMethod('start', start);
    client.onDeviceMethod('stop', stop);
    client.on('message', receiveMessageCallback);
    setInterval(sendMessage, 6000);
});
