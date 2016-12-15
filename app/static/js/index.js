(function(){
  	console.log('It goes until here');
	var ws = new WebSocket("ws://localhost:8888/vis");

	ws.onopen = function(){
	    ws.send("Sent message ok");
	};

	ws.onmessage = function(event) {
	    data_json = event.data;
	    console.log(data_json);
	};

})();