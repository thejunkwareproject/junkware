
function Terminal(_div,_header) {
    this.div = _div;
    this.header = _header;
    this.infiniteLoop =false;
}

Terminal.prototype.init = function(){
    console.log('init terminal');
    this.createCaret($(this.div));
    this.blink();
}

Terminal.prototype.createCaret = function(_div) {
    _div.append("<span class='blink'>|</span>");
}

Terminal.prototype.caret = function(){
    return $(this.div).find(".blink");
}

Terminal.prototype.blink = function(){
    $blink=this.caret();
    setInterval(function(){
            $blink = $('.blink').last();
            if( $blink.css('visibility')=='hidden' ){
                    $blink.css('visibility','visible');
            }else{
                    $blink.css('visibility','hidden');
            }
    },500);
}

Terminal.prototype.addMessage = function(_text){
    this.caret().remove();
    var from = this.header;
    var text = _text;

    var div = $("<div class='message'></div>");
    $(this.div).append(div);
    var self = this;
    div.append("<p class='terminal-header'>" + from + "</p>");
    div.find(".terminal-header").css("color", "green");

    //text
    var t = 0;
    if(text != '...' && text != undefined){
        var spli = splitTokens(text,'{}[|]><=%/\\');
        text = spli[0];

        t = Math.floor(Math.random()*600);
        setTimeout(function(){
            div.append("<p>" + text + (spli.length>1 ? "..." : "") + "</p> ");
            div.shuffleLetters();
            self.createCaret(div);
        }, t);
    }
    
    if(this.infiniteLoop ==true) {
        while($(this.div).height() > $(this.div+"-container").height()){
            $('.message').first().remove();
            // console.log($('#content').height(), window.innerHeight);
        }
    }
}

Terminal.prototype.addMessages = function(_text_array) {
        var data = _text_array; 
        console.log("messages : ",data.length);
        var self=this;
        var i =0;
        function messageTimeout() {
            setTimeout(function () {
                console.log(i);
                if(i < data.length) {
                    self.addMessage(data[i]);
                    i++;
                    messageTimeout();
                } else if ( i == data.length && this.infiniteLoop ==true) {
                    i=0;
                }
            }, 500+Math.floor(Math.random()>.8 ? 1000+Math.random()*2000 : Math.random()*1000));
        }
        messageTimeout();
        // for (i = 0; i < data.length; i++) {
            
        //     (function(ind) {
        //        setTimeout(function(){setContentOpacity(ind);}, (ind*3));
        //         setTimeout(autoAddMessage, 200); //

        //     })(i);
        // }

        // function autoAddMessage () {
        // }
}

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
