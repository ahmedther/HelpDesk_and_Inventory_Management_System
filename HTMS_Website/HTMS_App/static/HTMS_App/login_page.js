/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!******************************!*\
  !*** ./src/js/login_page.js ***!
  \******************************/
var deleteErrorFunc = function deleteErrorFunc() {
  var errorEl = document.querySelector('.error');
  setTimeout(function () {
    return errorEl.remove();
  }, 12 * 1000);
};
var scroller = function scroller() {
  var progress = document.querySelector(".progressbar");
  var totalHeight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function () {
    var progressHeight = window.pageYOffset / totalHeight * 100;
    progress.style.height = progressHeight + "%";
  };
};
deleteErrorFunc();
scroller();
/******/ })()
;
//# sourceMappingURL=login_page.js.map