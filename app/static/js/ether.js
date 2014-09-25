///////// VARIABLES
    var jsonFile="data/samples.json";
    var jsonsLoaded = false;

///////// ADD MESSAGES
    function initMessage(){
        console.log('initMessage');
        $('#terminal').append("<p class='blink'>|</p>");
    }

    // var images;
    function addMessage(jsonObject){
        $("p.blink").remove();

        // console.log(jsonObject);

        var from = jsonObject.from;
        // var geo = jsonObject.geo;
        // var images = jsonObject.images;
        var text = jsonObject.text;

        var div = $("<div class='message'></div>");
        $('#terminal').append(div);
        var t = 0;

        //From - To
        div.append("<p class='fromTo'>from " + from.toUpperCase() + "</p>");

        //text
        if(text != '...' && text != undefined){
            var spli = splitTokens(text,'{}[|]><=%/\\');
            text = spli[0];

            t = Math.floor(Math.random()*600);
            setTimeout(function(){
                div.append("<p>" + text + (spli.length>1 ? "..." : "") + "</p>");
            }, t);
        }

        function addCaret(){
            div.append("<p class='blink'>|</p>");
        }

        while($('#terminal').height() > $("#terminal-container").height()){
            $('.message').first().remove();
            // console.log($('#content').height(), window.innerHeight);
        }
    }

/////////BLINKING CARET
    function blink(){
        var $blink;
        setInterval(function(){
                $blink = $('.blink').last();
                if( $blink.css('visibility')=='hidden' ){
                        $blink.css('visibility','visible');
                }else{
                        $blink.css('visibility','hidden');
                }
        },500);
    }


/////////AUTO ADD MESSAGE FROM JSON

    var iterator = 0;
    var jsondata;
    function initAutoAddMessage(){
        console.log('initAutoAddMessage');
        $.ajax({
            type: 'GET',
            url: jsonFile,
            dataType: 'json',
            success: function(data) {
                jsondata=data;
                jsonsLoaded = true;
            },
            data: {},
            async: false
        });
    }
    
    function autoAddMessage(){
        // console.log('AutoAddMessage()');
        if(jsonsLoaded){
            // console.log(jsondata);
            // console.log('AutoAddMessage() OK');
            if(iterator < jsondata.samples.length-1){
                iterator++;
            }
            else{
                iterator = 0;
            }
            addMessage(jsondata.samples[iterator]);
        }
        setTimeout(autoAddMessage, 500+Math.floor(Math.random()>.8 ? 1000+Math.random()*2000 : Math.random()*1000));
    }
    autoAddMessage();
    
///////// ONLOAD
    function startMessaging (){
        initMessage();
        blink();
        initAutoAddMessage();
    };

////////SplitTokens function take from Processing.js
    function splitTokens(str, tokens) {
        var chars = tokens.split(/()/g),
            buffer = "",
            len = str.length,
            i, c,
            tokenized = [];

        for (i = 0; i < len; i++) {
            c = str[i];
            if (chars.indexOf(c) > -1) {
                if (buffer !== "") {
                    tokenized.push(buffer);
                }
                buffer = "";
            }
            else {
                buffer += c;
            }
        }

        if (buffer !== "") {
            tokenized.push(buffer);
        }

        return tokenized;
    }

/////////CONVERSION UTILS
    // from http://snipplr.com/view.php?codeview&id=52975
    function dec2Hex(d) {
        return d.toString(16);
    }

    function hex2Dec (h) {
        return parseInt(h, 16);
    }

    function string2Hex (tmp) {
        var str = '',
            i = 0,
            tmp_len = tmp.length,
            c;
        
        for (; i < tmp_len; i++) {
            c = tmp.charCodeAt(i);
            str += dec2Hex(c) + ' ';
        }
        return str;
    }

    function hex2String (tmp) {
        var arr = tmp.split(' '),
            str = '',
            i = 0,
            arr_len = arr.length,
            c;
        
        for (; i < arr_len; i++) {
            c = String.fromCharCode( hex2Dec( arr[i] ) );
            str += c;
        }
        
        return str;
    }

    function string2Bin(str){
        var st,i,j,d;
        var arr = [];
        var len = str.length;
        for (i = 1; i<=len; i++){
            //reverse so its like a stack
            d = str.charCodeAt(len-i);
            for (j = 0; j < 8; j++) {
                arr.push(d%2);
                d = Math.floor(d/2);
            }
        }
        //reverse all bits again.
        return arr.reverse().join("");
    }
