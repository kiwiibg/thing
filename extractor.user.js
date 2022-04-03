// ==UserScript==
// @name         Ritaly template extractor
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  la mentesciame is megli che uan!
// @author       mclochard
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener(
      "load",
      () => {
  
          const x = 782 ;
          const y = 254;
          const w = 84;
          const h = 238;
        document.getElementsByTagName("body")[0].appendChild(
          (function () {
            const i = document.createElement("button");
            i.style =
              "position: fixed;left: 10px; background: #fff; top: 30%;width: 50px;height: 50px;";
            i.innerHTML = "DL";
  
            function downloadURI(uri, name) {
              var link = document.createElement("a");
              link.download = name;
              link.href = uri;
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
              delete link;
            }
            function crop(dataUrl, x, y, w, h) {
              return canvas1.toDataURL();
            }
            i.onclick = function () {
              const dataUrl = document
                .getElementsByTagName("mona-lisa-embed")[0]
                .shadowRoot.children[0].getElementsByTagName(
                  "mona-lisa-canvas"
                )[0]
                .shadowRoot.children[0].getElementsByTagName("canvas")[0]
                .toDataURL();
  
              var canvas1 = document.createElement("canvas");
              var ctx1 = canvas1.getContext("2d");
              var img = new Image();
              img.onload = function () {
                ctx1.drawImage(img, x, y, w, h, 0, 0, w, h);
                downloadURI(canvas1.toDataURL(), "canvas.png");
              };
              img.src = dataUrl;
              canvas1.width = w;
              canvas1.height = h;
            };
            console.log(i);
            return i;
          })()
        );
      },
      false
    );
  }
  