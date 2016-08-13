// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var port = null;

var getKeys = function(obj){
   var keys = [];
   for(var key in obj){
      keys.push(key);
   }
   return keys;
}


function appendMessage(text) {
  document.getElementById('response').innerHTML += "<p>" + text + "</p>";
}

function updateUiState() {
  if (port) {
    document.getElementById('connect-button').style.display = 'none';
    document.getElementById('input-text').style.display = 'none';
    document.getElementById('send-message-button').style.display = 'none';
  } else {
    document.getElementById('connect-button').style.display = 'none';
    document.getElementById('input-text').style.display = 'none';
    document.getElementById('send-message-button').style.display = 'none';
  }
}

function sendNativeMessage() {
  //message = {"text": document.getElementById('input-text').value};
  //port.postMessage(message);
  //appendMessage("Sent message: <b>" + JSON.stringify(message) + "</b>");
}

function sendPythonMessage() {
  message = {"subfolder": document.getElementById('subfolder-name').value};
  port.postMessage(message);
}

function onNativeMessage(message) {
  appendMessage("Received message: <b>" + JSON.stringify(message) + "</b>");
}

function onDisconnected() {
  appendMessage("Failed to connect: " + chrome.runtime.lastError.message);
  port = null;
  updateUiState();
}

function connect() {

}

//update dropdown
function updateDropDown() {
  $(".drop2:first-child").html($(this).text()+ ' <span class="caret"></span>');
}

document.addEventListener('DOMContentLoaded', function () {
  //startup messaging port
  var hostName = "com.ytfiber";
  appendMessage("Connecting to native messaging host <b>" + hostName + "</b>")
  port = chrome.runtime.connectNative(hostName);
  port.onMessage.addListener(onNativeMessage);
  port.onDisconnect.addListener(onDisconnected);
  updateUiState();

  //document.getElementById('connect-button').addEventListener(
      //'click', connect);
  //document.getElementById('send-message-button').addEventListener(
    //  'click', sendNativeMessage);

  document.getElementById('download_btn').addEventListener(
      'click', sendPythonMessage);

  //$(".dropdown2 li a").click(function() {});
});
