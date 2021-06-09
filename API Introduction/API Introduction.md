# Introduction to Web APIs

First, we'll look at the basics of what an API is - how they work, how to use them in your code, how they are structured. We will also see what the main APIs are and how to use them.



> **Prerequisites:** Basic knowledge of computer science, basic understanding of HTML and CSS, notions of JavaScript.
>
> **Objective:** To familiarize yourself with APIs, what they can do, and how to use them in your code.



## What is an API?

**APIs (Application Programming Interfaces)** are constructs available in programming languages to allow developers to create complex functionality more easily. They take care of the more complex parts of code, providing the developer with easier-to-use syntax instead.

As a concrete example, think of electrical connections in a house, apartment or other dwelling. If you want to use an appliance in your house, you just plug it into an outlet and it works. You don't try to plug it directly into the power supply - doing so would be really inefficient, and, if you're not an electrician, difficult and dangerous to do.

Similarly, for example, when programming 3D graphics, it's much easier to do so using an API written in a high-level language like JavaScript or Python, rather than trying to write low-level code (like C or C+) that directly controls the computer's GPU or other graphics functions.

> **Note:**
>
> See also the glossary entry for the term API for more descriptions.



## Client-side JavaScript API

 Client-side JavaScript in particular has many APIs at its disposal - they are not part of the JavaScript language itself, they are built on top of JavaScript, offering additional superpowers to use in your code. They generally fall into one of two categories:

* Browser APIs are built into the web browser and make data from the browser and its environment available to do complex things with. For example, the Web Audio API provides JavaScript constructs to manipulate audio data in the browser. You can use this API to retrieve an audio track and then lower its volume, apply effects, etc. Under the hood, the browser takes care of the more complex layers of "low-level" code (C++ or Rust, for example) in order to perform the signal processing. Again, this complexity is masked by the abstraction offered by the API.

* Third-party APIs are not built into the browser by default, and you usually have to retrieve the API code and information from a website.

  

For example: the Twitter API allows you to display your latest tweets on your website. It provides a set of constructs that you can use to query the Twitter service, which then returns the requested information.



## Relationship between JavaScript, APIs and other JavaScript tools

Above, we've outlined what a client-side JavaScript API is and its relationship to the JavaScript language. To recap, clarify, and provide more detail on other JavaScript tools that exist:

* **JavaScript** - A high-level programming language built into browsers that enables functionality to be implemented on web pages and applications. Note that JavaScript is also available in other programming environments, such as Node. But don't worry about it for now.

* **Browser APIs** - Built-in constructs in the browser on top of JavaScript that allow for easier implementation of functionality.

* **Third-party APIs** - Constructs built into third-party platforms (e.g. Twitter, Facebook) that allow you to use some of the functionality of those platforms in your own web pages (e.g. display your latest Tweets on your web page).

* **JavaScript libraries** - Usually one or more JavaScript files containing custom functions that you can attach to your web page to speed up or enable the writing of common features. Examples include jQuery, Mootools and React.

* **JavaScript frameworks** - On top of libraries, JavaScript frameworks (e.g. Angular and Ember) are more like packages of HTML, CSS, JavaScript and other technologies, which you install and then use to write an entire web application.

The key difference between a library and a framework is "Reverse Control". With a library, it is the developer who calls the library's methods - he exercises control. With a framework, the control is reversed: the framework calls the developer's code.

 

# What can APIs do?

There are a lot of APIs available in modern browsers. They allow you to do a wide range of things. You can get an idea by taking a look at the MDN API index page.



## Common browser APIs

In particular, here are the most common categories of browser APIs you'll use (and which we'll look at in this module in more detail):

* **APIs for manipulating documents** loaded into the browser. The most obvious example is the **DOM** (Document Object Model) API. It allows you to manipulate HTML and CSS - create, delete and modify HTML code, apply new styles to your page dynamically, etc. For example, every time you see a pop-up window appear on a page, or new content displayed, the DOM is in action. Find out more about these types of APIs in the Manipulating Documents section.

* **APIs for retrieving data from the server** to update sections of a web page are commonly used. This seemingly trivial detail has had a huge impact on site performance and behavior - if you just need to update a product listing or display new items available, doing so instantly without having to reload the entire page from the server can make the site or application much more responsive and "eye-catching." XMLHttpRequest and the Fetch API are the APIs that make this possible. You may also see the term **Ajax** used to describe this technique. To learn more about these APIs, see Fetch Data from the Server.

* **APIs for drawing and manipulating graphics** are now commonly supported in browsers - the most popular are **Canvas** and **WebGL**. They allow programmatically updating the pixels contained in an HTML `<canvas>` element to create 2D and 3D scenes. For example, you can draw shapes like rectangles or circles, import an image onto the canvas, and apply a sepia or grayscale filter to it using the Canvas API, or create a complex 3D scene with lighting and textures using WebGL. Such APIs are often combined with other APIs, for example `window.requestAnimationFrame()`, to create animation loops (making continuous scene updates) and thus create cartoons and games. To learn more about these APIs, see Drawing graphical elements.

* **Audio and video APIs**, such as **HTMLMediaElement**, **Web Audio API** or **WebRTC**, allow you to do really interesting things with multimedia, such as creating custom UI controls to play audio and video, displaying text such as captions and subtitles, retrieving video from your webcam to display on another person's computer in a video conference or adding effects to audio tracks (such as gain, distortion, balance, etc.). To learn more about these APIs, see Audio and Video APIs.

* **Device APIs** essentially allow you to handle and retrieve data from modern devices in ways that are useful for web applications. We've already talked about the geolocation API accessing the device's location data so you can pinpoint your position on a map. Other examples include letting the user know that an update is available for a web application via system notifications (see Notifications API) or vibrations (see Vibration API).

* **Client-side storage APIs** are becoming increasingly common in web browsers - the ability to store data on the client side is very useful if you want to create an application that saves its state between page loads, and perhaps even runs when the device is offline. There are a number of options available, for example simple name/value storage with the Web Storage API, and more complex tabular data storage with the **IndexedDB API**. To learn more about these APIs, see Client-Side Storage.

 

## Common third-party APIs

There are a wide variety of third-party APIs. Here are some of the most popular ones that you'll probably use sooner or later:

* The **Twitter API** allows you to display your latest tweets on a website.

* Mapping APIs like **Mapquest** and **Google Maps API** allow you to make all kinds of maps in web pages.

* The **Facebook API** set allows you to use different parts of the Facebook ecosystem in your application (e.g. to connect to a Facebook account, manage payments or advertising, etc.).

* **Telegram APIs** allow you to integrate content from Telegram channels on a website and support bots.

* The **YouTube API** allows you to embed YouTube videos on your site, search YouTube, build playlists, etc.

* The **Pinterest API** provides tools to manage Pinterest boards and pins and include them on your website.

* The **Twilio API** provides a set of tools to integrate audio and video calling features into an application and/or send SMS/MMS.

* The **Mastodon API** allows you to manipulate the features of the Mastodon social network through programs.

 **Note:**

> You can find information on many more third-party APIs in the Programmable Web API directory.

 

# How do the APIs work? 

Each JavaScript API works slightly differently from another, but in general they have common features and similar themes.



## They are object-based

APIs interact with code using one or more JavaScript objects, which serve as containers for the data used by the API (contained in object properties), and the functionality made available by the API (contained in object methods).

> **Note:**
>
> If you are not already familiar with how objects work, you should go back and browse the JavaScript objects module before continuing.

 Let's take the **Web Audio API** as an example. This is a fairly complex API with several objects. Here are the main objects:

* `AudioContext`, which represents an audio graph that can be used in order to manipulate audio playback in the browser and has different methods and properties that are available to manipulate this audio signal.

* `MediaElementAudioSourceNode`, which represents an `<audio>` element containing audio that we want to play and manipulate in the context.

* `AudioDestinationNode`, which represents the destination of the audio, i.e., the physical component that will be used to produce the sound (this is usually the speakers or headphones).

 So how do these objects interact? If you look at our audio component example (also look at it live), you will see the following code:

 ```html
<audio src="outfoxing.mp3"></audio>
<button class="paused">Play</button>
<br>
<input type="range" min="0" max="1" step="0.01" value="1" class="volume">
 ```

Firstly, we include an `<audio>` element with which we embed an MP3 in the page. We do not include any default browser controls. Next, we include a `<button>` that we'll use to play and stop the music, and a range `<input>` element, which we'll use to adjust the volume of the track being played.

 Next, let's look at the JavaScript for this example.

 We start by creating an AudioContext instance inside which we'll manipulate our track:

``` js
const AudioContext = window.AudioContext || window.webkitAudioContext;

const audioCtx = new AudioContext();
```

Next, we create constants that store references to our `<audio>`, `<button>`, and `<input>` elements, and we use the `AudioContext.createMediaElementSource()` method to create a `MediaElementAudioSourceNode` representing the source of our audio - the `<audio>` element will be played from :

 ```js
const audioElement = document.querySelector('audio');

const playBtn = document.querySelector('button');

const volumeSlider = document.querySelector('.volume');

const audioSource = audioCtx.createMediaElementSource(audioElement);
 ```

Next, we include two event handlers that are used to toggle between play and pause when the button is pressed and to reset the display to the beginning when the song is over :

``` js
  playBtn.addEventListener('click', function() {

    // check if the context is in suspend state (autoplay policy)

    if (audioCtx.state === 'suspended') {

      audioCtx.resume();

    }

  
  // if the track is stopped, play it

    if (this.getAttribute('class') === 'paused') {

      audioElement.play();

      this.setAttribute('class', 'playing');

      this.textContent = 'Pause';

    // if a track is playing, stop it

  } else if (this.getAttribute('class') === 'playing') {

      audioElement.pause();

      this.setAttribute('class', 'paused');

      this.textContent = 'Play';

    }

  });

  // if the track ends

  audioElement.addEventListener('ended', function() {

    playBtn.setAttribute('class', 'paused');

    playBtn.textContent = 'Play';

  });
```

> **Note:**
>
> Some of you may have noticed that the `play()` and `pause()` methods used to play and pause the track are not part of the **Web Audio API**; they are part of the **HTMLMediaElement API**. which is different but closely related.

Next, we create a `GainNode` object using the `AudioContext.createGain()` method, which can be used to adjust the volume of the audio passing through it, and we create another event handler that changes the gain (volume) value of the audio graph when the slider value is changed:

```  js
const gainNode = audioCtx.createGain();

volumeSlider.addEventListener('input', function() {

  gainNode.gain.value = this.value;

});
```

The last thing you need to do to make this work is to connect the different nodes in the audio graph, which is done using the `AudioNode.connect()` method available on each node type:

 ```
audioSource.connect(gainNode).connect(audioCtx.destination);
 ```

The audio starts in the source, which is then connected to the gain node so that the volume of the audio can be adjusted. The gain node is then connected to the destination node so that the audio can be played back on your computer (the `AudioContext.destination` property represents what is the default `AudioDestinationNode` available on your computer's hardware, for example your speakers).



## They have recognizable entry points

When using an API, you need to make sure you know where the API entry point is. In the **Web Audio API**, this is pretty straightforward - it's the `AudioContext` object, which must be used to perform any kind of audio manipulation.

 The **DOM** (Document Object Model) API also has a simple entry point - its functionality tends to be found hooked into the `Document` object, or an instance of an HTML element that you want to affect in some way, for example:

 ```js
const em = document.createElement('em'); // create a new em element

const para = document.querySelector('p'); // reference an existing p element

em.textContent = 'Hello there!'; // give em some text content

para.appendChild(em); // embed em in the paragraph
 ```

The **Canvas API** also relies on getting a context object to use to manipulate things, although in this case it's a graphical context rather than an audio context. Its context object is created by getting a reference to the `<canvas>` element you want to draw on, then calling its `HTMLCanvasElement.getContext()` method:

 ```js
const canvas = document.querySelector('canvas');

const ctx = canvas.getContext('2d');
 ```

Everything we want to do to the canvas is then done by calling the properties and methods of the context object (which is an instance of `CanvasRenderingContext2D`), for example :

 ```js
Ball.prototype.draw = function() {

 ctx.beginPath();

 ctx.fillStyle = this.color;

 ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);

 ctx.fill();

};
 ```

> **Note :**
>
> You can see this code in action in our bouncing ball demo (see it working live too).

 

## They use events to handle state changes

 We have already covered events earlier in the course in our Introduction to Events article, which looks in detail at what client-side web events are and how they are used in your code. If you're not already familiar with how client-side web API events work, we recommend you read that article before proceeding.

Some Web APIs contain no events at all, but most contain at least a few. The handler properties that allow us to execute functions when events occur are usually listed in our reference material in separate sections called "Event Handlers".

We have already seen a number of event handlers used in our **Web Audio API** example above.

To provide another example, instances of the `XMLHttpRequest` object (each represents an HTTP request to the server to retrieve a new resource of a certain type) has a number of events available on them, for example, the load event is fired when a response has been successfully returned containing the requested resource, and it is now available.

The following code provides a simple example of how this can be used:

 ```js
let requestURL = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';

let request = new XMLHttpRequest();

request.open('GET', requestURL);

request.responseType = 'json';

request.send();

request.onload = function() {

 const superHeroes = request.response;

 populateHeader(superHeroes);

 showHeroes(superHeroes);

}
 ```



> **Note :**
>
> You can see this code in action in our ajax.html example (see it live too).

The first five lines specify the location of the resource we want to retrieve, create a new instance of a request object using the `XMLHttpRequest()` constructor, open an HTTP GET request to retrieve the specified resource, specify that the response should be sent in JSON format, and then send the request.

The onload handler function then specifies what we do with the response. We know that the response will be successfully returned and available after the load event is fired (unless an error occurred), so we save the response containing the returned JSON in the superHeroes variable, then pass it to two different functions for further processing.



## They have adequate additional security mechanisms

Web API functionality is subject to the same security considerations as JavaScript and other web technologies (e.g., same-origin policy), but sometimes they have additional security mechanisms. For example, some of the more modern Web APIs will only work on pages served over HTTPS because they transmit potentially sensitive data (e.g. Service Workers and Push).

In addition, some Web APIs require permission to be enabled from the user once calls to these interfaces are made in your code. As an example, the Notifications API asks for permission using a pop-up dialog:

**Web Audio** and **HTMLMediaElement APIs** are subject to a security mechanism called `autoplay policy` - this essentially means that you cannot automatically play audio when a page loads - you must allow your users to trigger audio playback through a control such as a button. This is done because automatic audio playback is generally very annoying and we should not subject our users to it.

 **Note:**

> Depending on the stringency of the browser, these security mechanisms may even prevent the example from running locally, that is, if you load the local example file into your browser instead of running it from a web server. At the time of writing, our **Audio Web API** example was not running locally on Google Chrome - we had to upload it to GitHub before it worked.

 

# Summary

At this point, you should have a good idea of what APIs are, how they work, and what you can do with them in your JavaScript code. You're probably eager to start doing fun things with specific APIs, so let's get started!