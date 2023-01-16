/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/js/helper.js":
/*!**************************!*\
  !*** ./src/js/helper.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "closeDropdown": () => (/* binding */ closeDropdown),
/* harmony export */   "profileRandomColor": () => (/* binding */ profileRandomColor),
/* harmony export */   "scroller": () => (/* binding */ scroller),
/* harmony export */   "status_update": () => (/* binding */ status_update)
/* harmony export */ });
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _regeneratorRuntime() { "use strict"; /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */ _regeneratorRuntime = function _regeneratorRuntime() { return exports; }; var exports = {}, Op = Object.prototype, hasOwn = Op.hasOwnProperty, defineProperty = Object.defineProperty || function (obj, key, desc) { obj[key] = desc.value; }, $Symbol = "function" == typeof Symbol ? Symbol : {}, iteratorSymbol = $Symbol.iterator || "@@iterator", asyncIteratorSymbol = $Symbol.asyncIterator || "@@asyncIterator", toStringTagSymbol = $Symbol.toStringTag || "@@toStringTag"; function define(obj, key, value) { return Object.defineProperty(obj, key, { value: value, enumerable: !0, configurable: !0, writable: !0 }), obj[key]; } try { define({}, ""); } catch (err) { define = function define(obj, key, value) { return obj[key] = value; }; } function wrap(innerFn, outerFn, self, tryLocsList) { var protoGenerator = outerFn && outerFn.prototype instanceof Generator ? outerFn : Generator, generator = Object.create(protoGenerator.prototype), context = new Context(tryLocsList || []); return defineProperty(generator, "_invoke", { value: makeInvokeMethod(innerFn, self, context) }), generator; } function tryCatch(fn, obj, arg) { try { return { type: "normal", arg: fn.call(obj, arg) }; } catch (err) { return { type: "throw", arg: err }; } } exports.wrap = wrap; var ContinueSentinel = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} var IteratorPrototype = {}; define(IteratorPrototype, iteratorSymbol, function () { return this; }); var getProto = Object.getPrototypeOf, NativeIteratorPrototype = getProto && getProto(getProto(values([]))); NativeIteratorPrototype && NativeIteratorPrototype !== Op && hasOwn.call(NativeIteratorPrototype, iteratorSymbol) && (IteratorPrototype = NativeIteratorPrototype); var Gp = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(IteratorPrototype); function defineIteratorMethods(prototype) { ["next", "throw", "return"].forEach(function (method) { define(prototype, method, function (arg) { return this._invoke(method, arg); }); }); } function AsyncIterator(generator, PromiseImpl) { function invoke(method, arg, resolve, reject) { var record = tryCatch(generator[method], generator, arg); if ("throw" !== record.type) { var result = record.arg, value = result.value; return value && "object" == _typeof(value) && hasOwn.call(value, "__await") ? PromiseImpl.resolve(value.__await).then(function (value) { invoke("next", value, resolve, reject); }, function (err) { invoke("throw", err, resolve, reject); }) : PromiseImpl.resolve(value).then(function (unwrapped) { result.value = unwrapped, resolve(result); }, function (error) { return invoke("throw", error, resolve, reject); }); } reject(record.arg); } var previousPromise; defineProperty(this, "_invoke", { value: function value(method, arg) { function callInvokeWithMethodAndArg() { return new PromiseImpl(function (resolve, reject) { invoke(method, arg, resolve, reject); }); } return previousPromise = previousPromise ? previousPromise.then(callInvokeWithMethodAndArg, callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg(); } }); } function makeInvokeMethod(innerFn, self, context) { var state = "suspendedStart"; return function (method, arg) { if ("executing" === state) throw new Error("Generator is already running"); if ("completed" === state) { if ("throw" === method) throw arg; return doneResult(); } for (context.method = method, context.arg = arg;;) { var delegate = context.delegate; if (delegate) { var delegateResult = maybeInvokeDelegate(delegate, context); if (delegateResult) { if (delegateResult === ContinueSentinel) continue; return delegateResult; } } if ("next" === context.method) context.sent = context._sent = context.arg;else if ("throw" === context.method) { if ("suspendedStart" === state) throw state = "completed", context.arg; context.dispatchException(context.arg); } else "return" === context.method && context.abrupt("return", context.arg); state = "executing"; var record = tryCatch(innerFn, self, context); if ("normal" === record.type) { if (state = context.done ? "completed" : "suspendedYield", record.arg === ContinueSentinel) continue; return { value: record.arg, done: context.done }; } "throw" === record.type && (state = "completed", context.method = "throw", context.arg = record.arg); } }; } function maybeInvokeDelegate(delegate, context) { var methodName = context.method, method = delegate.iterator[methodName]; if (undefined === method) return context.delegate = null, "throw" === methodName && delegate.iterator["return"] && (context.method = "return", context.arg = undefined, maybeInvokeDelegate(delegate, context), "throw" === context.method) || "return" !== methodName && (context.method = "throw", context.arg = new TypeError("The iterator does not provide a '" + methodName + "' method")), ContinueSentinel; var record = tryCatch(method, delegate.iterator, context.arg); if ("throw" === record.type) return context.method = "throw", context.arg = record.arg, context.delegate = null, ContinueSentinel; var info = record.arg; return info ? info.done ? (context[delegate.resultName] = info.value, context.next = delegate.nextLoc, "return" !== context.method && (context.method = "next", context.arg = undefined), context.delegate = null, ContinueSentinel) : info : (context.method = "throw", context.arg = new TypeError("iterator result is not an object"), context.delegate = null, ContinueSentinel); } function pushTryEntry(locs) { var entry = { tryLoc: locs[0] }; 1 in locs && (entry.catchLoc = locs[1]), 2 in locs && (entry.finallyLoc = locs[2], entry.afterLoc = locs[3]), this.tryEntries.push(entry); } function resetTryEntry(entry) { var record = entry.completion || {}; record.type = "normal", delete record.arg, entry.completion = record; } function Context(tryLocsList) { this.tryEntries = [{ tryLoc: "root" }], tryLocsList.forEach(pushTryEntry, this), this.reset(!0); } function values(iterable) { if (iterable) { var iteratorMethod = iterable[iteratorSymbol]; if (iteratorMethod) return iteratorMethod.call(iterable); if ("function" == typeof iterable.next) return iterable; if (!isNaN(iterable.length)) { var i = -1, next = function next() { for (; ++i < iterable.length;) { if (hasOwn.call(iterable, i)) return next.value = iterable[i], next.done = !1, next; } return next.value = undefined, next.done = !0, next; }; return next.next = next; } } return { next: doneResult }; } function doneResult() { return { value: undefined, done: !0 }; } return GeneratorFunction.prototype = GeneratorFunctionPrototype, defineProperty(Gp, "constructor", { value: GeneratorFunctionPrototype, configurable: !0 }), defineProperty(GeneratorFunctionPrototype, "constructor", { value: GeneratorFunction, configurable: !0 }), GeneratorFunction.displayName = define(GeneratorFunctionPrototype, toStringTagSymbol, "GeneratorFunction"), exports.isGeneratorFunction = function (genFun) { var ctor = "function" == typeof genFun && genFun.constructor; return !!ctor && (ctor === GeneratorFunction || "GeneratorFunction" === (ctor.displayName || ctor.name)); }, exports.mark = function (genFun) { return Object.setPrototypeOf ? Object.setPrototypeOf(genFun, GeneratorFunctionPrototype) : (genFun.__proto__ = GeneratorFunctionPrototype, define(genFun, toStringTagSymbol, "GeneratorFunction")), genFun.prototype = Object.create(Gp), genFun; }, exports.awrap = function (arg) { return { __await: arg }; }, defineIteratorMethods(AsyncIterator.prototype), define(AsyncIterator.prototype, asyncIteratorSymbol, function () { return this; }), exports.AsyncIterator = AsyncIterator, exports.async = function (innerFn, outerFn, self, tryLocsList, PromiseImpl) { void 0 === PromiseImpl && (PromiseImpl = Promise); var iter = new AsyncIterator(wrap(innerFn, outerFn, self, tryLocsList), PromiseImpl); return exports.isGeneratorFunction(outerFn) ? iter : iter.next().then(function (result) { return result.done ? result.value : iter.next(); }); }, defineIteratorMethods(Gp), define(Gp, toStringTagSymbol, "Generator"), define(Gp, iteratorSymbol, function () { return this; }), define(Gp, "toString", function () { return "[object Generator]"; }), exports.keys = function (val) { var object = Object(val), keys = []; for (var key in object) { keys.push(key); } return keys.reverse(), function next() { for (; keys.length;) { var key = keys.pop(); if (key in object) return next.value = key, next.done = !1, next; } return next.done = !0, next; }; }, exports.values = values, Context.prototype = { constructor: Context, reset: function reset(skipTempReset) { if (this.prev = 0, this.next = 0, this.sent = this._sent = undefined, this.done = !1, this.delegate = null, this.method = "next", this.arg = undefined, this.tryEntries.forEach(resetTryEntry), !skipTempReset) for (var name in this) { "t" === name.charAt(0) && hasOwn.call(this, name) && !isNaN(+name.slice(1)) && (this[name] = undefined); } }, stop: function stop() { this.done = !0; var rootRecord = this.tryEntries[0].completion; if ("throw" === rootRecord.type) throw rootRecord.arg; return this.rval; }, dispatchException: function dispatchException(exception) { if (this.done) throw exception; var context = this; function handle(loc, caught) { return record.type = "throw", record.arg = exception, context.next = loc, caught && (context.method = "next", context.arg = undefined), !!caught; } for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i], record = entry.completion; if ("root" === entry.tryLoc) return handle("end"); if (entry.tryLoc <= this.prev) { var hasCatch = hasOwn.call(entry, "catchLoc"), hasFinally = hasOwn.call(entry, "finallyLoc"); if (hasCatch && hasFinally) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } else if (hasCatch) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); } else { if (!hasFinally) throw new Error("try statement without catch or finally"); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } } } }, abrupt: function abrupt(type, arg) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc <= this.prev && hasOwn.call(entry, "finallyLoc") && this.prev < entry.finallyLoc) { var finallyEntry = entry; break; } } finallyEntry && ("break" === type || "continue" === type) && finallyEntry.tryLoc <= arg && arg <= finallyEntry.finallyLoc && (finallyEntry = null); var record = finallyEntry ? finallyEntry.completion : {}; return record.type = type, record.arg = arg, finallyEntry ? (this.method = "next", this.next = finallyEntry.finallyLoc, ContinueSentinel) : this.complete(record); }, complete: function complete(record, afterLoc) { if ("throw" === record.type) throw record.arg; return "break" === record.type || "continue" === record.type ? this.next = record.arg : "return" === record.type ? (this.rval = this.arg = record.arg, this.method = "return", this.next = "end") : "normal" === record.type && afterLoc && (this.next = afterLoc), ContinueSentinel; }, finish: function finish(finallyLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.finallyLoc === finallyLoc) return this.complete(entry.completion, entry.afterLoc), resetTryEntry(entry), ContinueSentinel; } }, "catch": function _catch(tryLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc === tryLoc) { var record = entry.completion; if ("throw" === record.type) { var thrown = record.arg; resetTryEntry(entry); } return thrown; } } throw new Error("illegal catch attempt"); }, delegateYield: function delegateYield(iterable, resultName, nextLoc) { return this.delegate = { iterator: values(iterable), resultName: resultName, nextLoc: nextLoc }, "next" === this.method && (this.arg = undefined), ContinueSentinel; } }, exports; }
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }
function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }
var scroller = function scroller() {
  var progress = document.querySelector(".progressbar");
  var totalHeight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function () {
    var progressHeight = window.pageYOffset / totalHeight * 100;
    progress.style.height = progressHeight + "%";
  };
};
var randomColorNumber = function randomColorNumber() {
  var color = Math.floor(Math.random() * 256);
  return color;
};
var profileRandomColor = function profileRandomColor() {
  var profileElement = document.querySelectorAll(".requester-profile-photo");
  profileElement.forEach(function (el) {
    return colorChanger(el);
  });
  var paginateEl = document.querySelectorAll(".page-active");
  paginateEl.forEach(function (el) {
    return colorChanger(el);
  });
};
function colorChanger(el) {
  // const a = el.parentNode.parentNode.children[4].firstElementChild
  // const b = getComputedStyle(a)
  // const c = b['background']
  // const red = randomColorNumber()
  // const red1 = randomColorNumber()
  // const blue = randomColorNumber()
  // const blue1 = randomColorNumber()
  // const green = randomColorNumber()
  // const green1 = randomColorNumber()
  //  el.style.background = `linear-gradient(138deg, rgba(${red}, ${blue}, ${green}, 1) 0%, rgba(${red1}, ${blue1}, ${green1}, 1) 100% )`
  var colorList = ["#fca311",
  //yellow
  "#FFDD00",
  // yellow light
  "#FF4301",
  //orange dark
  "#F66B0E",
  //orange light
  "#ff006e",
  // dark pink
  "#F806CC",
  // light pink
  "#31E1F7",
  // sky blue
  "#0096FF",
  // blue
  "#00B7A8",
  // aqua blue teal
  "#3DB2FF",
  //light blue
  "#113CFC",
  // cco blue
  "#3B44F6",
  // indigo
  "#000000",
  //dark black
  "#4C0070",
  // dark purple
  "#8200FF",
  // light purple
  "#45046A",
  //violet
  "#FF0000",
  //red
  "#379237",
  //dark green
  "#49FF00",
  // light green
  "#A6CB12",
  //off green
  '#864000',
  //brown
  "#290001",
  // dark brown
  "#6A492B",
  //chikku brown
  "#696464",
  //grey dark
  "#414141",
  //grey light
  "#FF7F5B" // peach
  ];

  var color = Math.floor(Math.random() * colorList.length);
  //const color1 = Math.floor(Math.random() * colorList.length);
  // el.style.background = colorList[color]
  var backGradient = "linear-gradient(138deg, ".concat(colorList[color], "90 0%, ").concat(colorList[color], " 100%)");
  el.style.background = backGradient;
  // el.style.background = colorList[color];
  //el.style.background = c
}

function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1, c.length);
    }
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}
var status_update = /*#__PURE__*/function () {
  var _ref = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee() {
    return _regeneratorRuntime().wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            _context.next = 2;
            return fetch('http://127.0.0.1:8000/api/get_status/?format=json').then(function (response) {
              return response.json();
            }).then(function (data) {
              return status_working(data);
            });
          case 2:
          case "end":
            return _context.stop();
        }
      }
    }, _callee);
  }));
  return function status_update() {
    return _ref.apply(this, arguments);
  };
}();
var status_working = function status_working(data1) {
  var data = data1;
  data = data1.filter(function (item) {
    if (item.status_name == 'Open' || item.status_name == 'Assigned') return null;else return item.status_name;
  });
  var csrftoken = readCookie('csrftoken');
  var slugify = __webpack_require__(/*! slugify */ "./node_modules/slugify/slugify.js");
  var html = data.map(function (status) {
    return status_html(status, slugify);
  });
  var statusEL = document.querySelectorAll('.display-ticket-status');
  statusEL.forEach(function (el) {
    return status_instert(el, html, csrftoken, slugify);
  });
};
var status_html = function status_html(status, slugify) {
  var html = "<a data-status-value=\"".concat(status.status_name, "\"class=\"change-status--link\" href=\"#\">\n                      <div class=\"display-status-").concat(slugify(status.status_name).toLowerCase(), "\">\n                          <div class='display-status-text'>").concat(status.status_name, "</div>\n                      </div>\n                  </a>");
  return html;
};
var status_instert = function status_instert(el, html, csrftoken, slugify) {
  if (el.previousElementSibling.firstElementChild.innerHTML == 'None' || el.querySelector('.display-status-text').innerHTML == 'Closed' || el.classList.contains("non_it")) {
    return;
  }
  el.addEventListener('click', function (e) {
    return statusEvent(e, el, html, csrftoken, slugify);
  });
};
function statusEvent(e, el, html, csrftoken, slugify) {
  e.preventDefault();
  deleteTextArea();
  delete_dropDown();
  if (el.querySelector('.display-status-text').innerHTML == 'Closed') {
    return;
  }
  el.insertAdjacentHTML('beforebegin', "<div class=\"change-status--container\">" + html.join("") + "</div>");
  dropdownBtnClick(el, csrftoken, slugify);
}
function dropdownBtnClick(status_element, csrftoken, slugify) {
  var dropdownBtn = document.querySelectorAll(".change-status--link");
  dropdownBtn.forEach(function (el) {
    return status_post_request(el, status_element, csrftoken, slugify);
  });
}
var status_post_request = function status_post_request(el, status_element, csrftoken, slugify) {
  el.addEventListener('click', function (e) {
    post_format(e, el, status_element, csrftoken, slugify);
  });
};
var post_format = /*#__PURE__*/function () {
  var _ref2 = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee2(e, el, status_element, csrftoken, slugify) {
    var el_id;
    return _regeneratorRuntime().wrap(function _callee2$(_context2) {
      while (1) {
        switch (_context2.prev = _context2.next) {
          case 0:
            e.preventDefault();
            el_id = el.closest('.ticket-main-row');
            if (el.dataset.statusValue == 'On Hold') {
              onHoldReason(el_id, el, status_element, csrftoken, slugify);
            }
            if (el.dataset.statusValue != 'On Hold') post_to_databae(el_id, el, status_element, csrftoken, slugify);
          case 4:
          case "end":
            return _context2.stop();
        }
      }
    }, _callee2);
  }));
  return function post_format(_x, _x2, _x3, _x4, _x5) {
    return _ref2.apply(this, arguments);
  };
}();
function post_to_databae(_x6, _x7, _x8, _x9, _x10) {
  return _post_to_databae.apply(this, arguments);
}
function _post_to_databae() {
  _post_to_databae = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee3(el_id, el, status_element, csrftoken, slugify) {
    return _regeneratorRuntime().wrap(function _callee3$(_context3) {
      while (1) {
        switch (_context3.prev = _context3.next) {
          case 0:
            _context3.next = 2;
            return fetch("http://127.0.0.1:8000/api/post_status/", {
              // Adding method type
              method: "POST",
              // Adding body or contents to send
              body: JSON.stringify({
                id: el_id.dataset.id,
                status: el.dataset.statusValue
              }),
              // Adding headers to the request
              headers: {
                "Content-type": "application/json; charset=UTF-8",
                "X-CSRFToken": csrftoken
              }
            })

            // Converting to JSON
            // .then(response => response.json())

            // Displaying results to console
            .then(function (response) {
              // console.log(json)
              status_element.firstElementChild.classList = "display-status-".concat(slugify(el.dataset.statusValue).toLowerCase());
              delete_dropDown();
              status_element.querySelector('.display-status-text').innerHTML = el.dataset.statusValue;
            });
          case 2:
          case "end":
            return _context3.stop();
        }
      }
    }, _callee3);
  }));
  return _post_to_databae.apply(this, arguments);
}
function delete_dropDown() {
  var drop_container = document.querySelectorAll('.change-status--container');
  drop_container.forEach(function (el) {
    return addAnimeDelete(el);
  });
}
function deleteTextArea() {
  var reasonTextArea = document.querySelectorAll('.on-hold--post');
  reasonTextArea.forEach(function (el) {
    return addAnimeDelete(el);
  });
}
var addAnimeDelete = function addAnimeDelete(el) {
  el.style.animation = '500ms dropdownStatusFade';
  setTimeout(removefunc, '500', el);
};
var removefunc = function removefunc(el) {
  el.remove();
};
var onHoldReason = function onHoldReason(el_id, el, status_element, csrftoken, slugify) {
  var onHoldHtml = "<div class=\"on-hold--post\">\n  <label  class='on-hold--label' for='description'>Reason for The Hold</label>\n  <textarea autofocus class='on-hold--post-textarea' rows=\"5\" cols=\"33\" type=\"text\" name=\"description\" id=\"description\"\n    placeholder=\"Why is this issue put on hold?\"></textarea>\n  <button type='submit' class='on-hold--submit-button'>\n      <span class='btn--add btn--text'>Submit</span>\n  </button>\n</div>";
  var holdCont = el.closest('.ticket-main-row');
  var tick_stat = holdCont.querySelector('.display-ticket-status');
  tick_stat.insertAdjacentHTML('beforebegin', onHoldHtml);
  var textarea = document.querySelector('.on-hold--post');
  textarea.addEventListener('click', function (e) {
    e.preventDefault();
    var textvalueEl = this.querySelector('.on-hold--post-textarea');
    var submitButton = document.querySelector('.on-hold--submit-button');
    submitButton.removeEventListener('click', postReasonToDb);
    submitButton.addEventListener('click', postReasonToDb(e, textvalueEl, holdCont, el_id, el, status_element, csrftoken, slugify));
  });
};
var postReasonToDb = function postReasonToDb(e, textvalueEl, holdCont, el_id, el, status_element, csrftoken, slugify) {
  e.preventDefault();
  if (textvalueEl.value) fetch("http://127.0.0.1:8000/api/post_reason_on_hold/", {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
      id: holdCont.dataset.id,
      reson_for_hold: textvalueEl.value
    }),
    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      "X-CSRFToken": csrftoken
    }
  })

  // Converting to JSON
  // .then(response => response.json()).then((json) => console.log(json))
  .then(function (response) {
    return deleteTextArea();
  }).then(function (res) {
    return post_to_databae(el_id, el, status_element, csrftoken, slugify);
  });
};
function closeDropdown() {
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.display-ticket-status') && !e.target.closest('.change-status--container') && !e.target.closest('.on-hold--post')) {
      deleteTextArea();
      delete_dropDown();
    }
  });
}

// export function paginationBtnClick() {
//   const search_box = document.getElementById('search-box-id')
//   const pagi_btn = document.querySelectorAll('.pagi-link')
//   if (search_box) {
//     pagi_btn.forEach(function (el) {

//       el.addEventListener('click', (e) => {
//         e.preventDefault()
//         const targetEl = el.closest('.pagi-link')
//         search_box.innerHTML += `<input value='${targetEl.dataset.page}' name='page' hidden>`x
//         search_box.submit()

//       })
//     })
//   }
// }

// import * as pg from 'pg';  // import pg

// const { Client } = require('pg')

// const client = new Client({
//     user: "postgres",
//     host: "172.20.100.81",
//     database: "HTMS_database",
//     password: "ahmed",
//     port: "5432",
// })

// client.connect();

// client.query(`SELECT * FROM public."HTMS_App_requests"
// ORDER BY id ASC `, (err, result) => {
//     if (err) {
//         console.log(err.message);
//     }
//     else {
//         console.log(result.rows);
//     }
// })
// let test
// const status_update = async function () {
//   await fetch('http://127.0.0.1:8000/api/get_status/?format=json').then(function (response) {
//     return response.json()
//   }).then(function (data) {

//     const ne1w = data.map(function (status) {
//       const slugify = require('slugify')
//       let html = `<li><div class="display-status-${slugify(status.status_name).toLowerCase()}">
//                         <div class='display-status-text'>${status.status_name}</div>
//                       </div>
//                   </li>`
//       return html
//     }
//     )
//     test = ne1w
//   })

// }

// const statusEL = document.querySelectorAll('.display-ticket-status');
// statusEL.forEach(function (el) {
//   el.addEventListener('click', function (e) {
//     e.preventDefault();
//     console.log(test[0])
//     el.insertAdjacentHTML('afterbegin', `<ul class="change-status--container">` + test.join("") + ` </ul >`
//     )
//   }

//   )
// }

// )

/***/ }),

/***/ "./node_modules/slugify/slugify.js":
/*!*****************************************!*\
  !*** ./node_modules/slugify/slugify.js ***!
  \*****************************************/
/***/ (function(module) {


;(function (name, root, factory) {
  if (true) {
    module.exports = factory()
    module.exports["default"] = factory()
  }
  /* istanbul ignore next */
  else {}
}('slugify', this, function () {
  var charMap = JSON.parse('{"$":"dollar","%":"percent","&":"and","<":"less",">":"greater","|":"or","¢":"cent","£":"pound","¤":"currency","¥":"yen","©":"(c)","ª":"a","®":"(r)","º":"o","À":"A","Á":"A","Â":"A","Ã":"A","Ä":"A","Å":"A","Æ":"AE","Ç":"C","È":"E","É":"E","Ê":"E","Ë":"E","Ì":"I","Í":"I","Î":"I","Ï":"I","Ð":"D","Ñ":"N","Ò":"O","Ó":"O","Ô":"O","Õ":"O","Ö":"O","Ø":"O","Ù":"U","Ú":"U","Û":"U","Ü":"U","Ý":"Y","Þ":"TH","ß":"ss","à":"a","á":"a","â":"a","ã":"a","ä":"a","å":"a","æ":"ae","ç":"c","è":"e","é":"e","ê":"e","ë":"e","ì":"i","í":"i","î":"i","ï":"i","ð":"d","ñ":"n","ò":"o","ó":"o","ô":"o","õ":"o","ö":"o","ø":"o","ù":"u","ú":"u","û":"u","ü":"u","ý":"y","þ":"th","ÿ":"y","Ā":"A","ā":"a","Ă":"A","ă":"a","Ą":"A","ą":"a","Ć":"C","ć":"c","Č":"C","č":"c","Ď":"D","ď":"d","Đ":"DJ","đ":"dj","Ē":"E","ē":"e","Ė":"E","ė":"e","Ę":"e","ę":"e","Ě":"E","ě":"e","Ğ":"G","ğ":"g","Ģ":"G","ģ":"g","Ĩ":"I","ĩ":"i","Ī":"i","ī":"i","Į":"I","į":"i","İ":"I","ı":"i","Ķ":"k","ķ":"k","Ļ":"L","ļ":"l","Ľ":"L","ľ":"l","Ł":"L","ł":"l","Ń":"N","ń":"n","Ņ":"N","ņ":"n","Ň":"N","ň":"n","Ō":"O","ō":"o","Ő":"O","ő":"o","Œ":"OE","œ":"oe","Ŕ":"R","ŕ":"r","Ř":"R","ř":"r","Ś":"S","ś":"s","Ş":"S","ş":"s","Š":"S","š":"s","Ţ":"T","ţ":"t","Ť":"T","ť":"t","Ũ":"U","ũ":"u","Ū":"u","ū":"u","Ů":"U","ů":"u","Ű":"U","ű":"u","Ų":"U","ų":"u","Ŵ":"W","ŵ":"w","Ŷ":"Y","ŷ":"y","Ÿ":"Y","Ź":"Z","ź":"z","Ż":"Z","ż":"z","Ž":"Z","ž":"z","Ə":"E","ƒ":"f","Ơ":"O","ơ":"o","Ư":"U","ư":"u","ǈ":"LJ","ǉ":"lj","ǋ":"NJ","ǌ":"nj","Ș":"S","ș":"s","Ț":"T","ț":"t","ə":"e","˚":"o","Ά":"A","Έ":"E","Ή":"H","Ί":"I","Ό":"O","Ύ":"Y","Ώ":"W","ΐ":"i","Α":"A","Β":"B","Γ":"G","Δ":"D","Ε":"E","Ζ":"Z","Η":"H","Θ":"8","Ι":"I","Κ":"K","Λ":"L","Μ":"M","Ν":"N","Ξ":"3","Ο":"O","Π":"P","Ρ":"R","Σ":"S","Τ":"T","Υ":"Y","Φ":"F","Χ":"X","Ψ":"PS","Ω":"W","Ϊ":"I","Ϋ":"Y","ά":"a","έ":"e","ή":"h","ί":"i","ΰ":"y","α":"a","β":"b","γ":"g","δ":"d","ε":"e","ζ":"z","η":"h","θ":"8","ι":"i","κ":"k","λ":"l","μ":"m","ν":"n","ξ":"3","ο":"o","π":"p","ρ":"r","ς":"s","σ":"s","τ":"t","υ":"y","φ":"f","χ":"x","ψ":"ps","ω":"w","ϊ":"i","ϋ":"y","ό":"o","ύ":"y","ώ":"w","Ё":"Yo","Ђ":"DJ","Є":"Ye","І":"I","Ї":"Yi","Ј":"J","Љ":"LJ","Њ":"NJ","Ћ":"C","Џ":"DZ","А":"A","Б":"B","В":"V","Г":"G","Д":"D","Е":"E","Ж":"Zh","З":"Z","И":"I","Й":"J","К":"K","Л":"L","М":"M","Н":"N","О":"O","П":"P","Р":"R","С":"S","Т":"T","У":"U","Ф":"F","Х":"H","Ц":"C","Ч":"Ch","Ш":"Sh","Щ":"Sh","Ъ":"U","Ы":"Y","Ь":"","Э":"E","Ю":"Yu","Я":"Ya","а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ж":"zh","з":"z","и":"i","й":"j","к":"k","л":"l","м":"m","н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"h","ц":"c","ч":"ch","ш":"sh","щ":"sh","ъ":"u","ы":"y","ь":"","э":"e","ю":"yu","я":"ya","ё":"yo","ђ":"dj","є":"ye","і":"i","ї":"yi","ј":"j","љ":"lj","њ":"nj","ћ":"c","ѝ":"u","џ":"dz","Ґ":"G","ґ":"g","Ғ":"GH","ғ":"gh","Қ":"KH","қ":"kh","Ң":"NG","ң":"ng","Ү":"UE","ү":"ue","Ұ":"U","ұ":"u","Һ":"H","һ":"h","Ә":"AE","ә":"ae","Ө":"OE","ө":"oe","Ա":"A","Բ":"B","Գ":"G","Դ":"D","Ե":"E","Զ":"Z","Է":"E\'","Ը":"Y\'","Թ":"T\'","Ժ":"JH","Ի":"I","Լ":"L","Խ":"X","Ծ":"C\'","Կ":"K","Հ":"H","Ձ":"D\'","Ղ":"GH","Ճ":"TW","Մ":"M","Յ":"Y","Ն":"N","Շ":"SH","Չ":"CH","Պ":"P","Ջ":"J","Ռ":"R\'","Ս":"S","Վ":"V","Տ":"T","Ր":"R","Ց":"C","Փ":"P\'","Ք":"Q\'","Օ":"O\'\'","Ֆ":"F","և":"EV","ء":"a","آ":"aa","أ":"a","ؤ":"u","إ":"i","ئ":"e","ا":"a","ب":"b","ة":"h","ت":"t","ث":"th","ج":"j","ح":"h","خ":"kh","د":"d","ذ":"th","ر":"r","ز":"z","س":"s","ش":"sh","ص":"s","ض":"dh","ط":"t","ظ":"z","ع":"a","غ":"gh","ف":"f","ق":"q","ك":"k","ل":"l","م":"m","ن":"n","ه":"h","و":"w","ى":"a","ي":"y","ً":"an","ٌ":"on","ٍ":"en","َ":"a","ُ":"u","ِ":"e","ْ":"","٠":"0","١":"1","٢":"2","٣":"3","٤":"4","٥":"5","٦":"6","٧":"7","٨":"8","٩":"9","پ":"p","چ":"ch","ژ":"zh","ک":"k","گ":"g","ی":"y","۰":"0","۱":"1","۲":"2","۳":"3","۴":"4","۵":"5","۶":"6","۷":"7","۸":"8","۹":"9","฿":"baht","ა":"a","ბ":"b","გ":"g","დ":"d","ე":"e","ვ":"v","ზ":"z","თ":"t","ი":"i","კ":"k","ლ":"l","მ":"m","ნ":"n","ო":"o","პ":"p","ჟ":"zh","რ":"r","ს":"s","ტ":"t","უ":"u","ფ":"f","ქ":"k","ღ":"gh","ყ":"q","შ":"sh","ჩ":"ch","ც":"ts","ძ":"dz","წ":"ts","ჭ":"ch","ხ":"kh","ჯ":"j","ჰ":"h","Ṣ":"S","ṣ":"s","Ẁ":"W","ẁ":"w","Ẃ":"W","ẃ":"w","Ẅ":"W","ẅ":"w","ẞ":"SS","Ạ":"A","ạ":"a","Ả":"A","ả":"a","Ấ":"A","ấ":"a","Ầ":"A","ầ":"a","Ẩ":"A","ẩ":"a","Ẫ":"A","ẫ":"a","Ậ":"A","ậ":"a","Ắ":"A","ắ":"a","Ằ":"A","ằ":"a","Ẳ":"A","ẳ":"a","Ẵ":"A","ẵ":"a","Ặ":"A","ặ":"a","Ẹ":"E","ẹ":"e","Ẻ":"E","ẻ":"e","Ẽ":"E","ẽ":"e","Ế":"E","ế":"e","Ề":"E","ề":"e","Ể":"E","ể":"e","Ễ":"E","ễ":"e","Ệ":"E","ệ":"e","Ỉ":"I","ỉ":"i","Ị":"I","ị":"i","Ọ":"O","ọ":"o","Ỏ":"O","ỏ":"o","Ố":"O","ố":"o","Ồ":"O","ồ":"o","Ổ":"O","ổ":"o","Ỗ":"O","ỗ":"o","Ộ":"O","ộ":"o","Ớ":"O","ớ":"o","Ờ":"O","ờ":"o","Ở":"O","ở":"o","Ỡ":"O","ỡ":"o","Ợ":"O","ợ":"o","Ụ":"U","ụ":"u","Ủ":"U","ủ":"u","Ứ":"U","ứ":"u","Ừ":"U","ừ":"u","Ử":"U","ử":"u","Ữ":"U","ữ":"u","Ự":"U","ự":"u","Ỳ":"Y","ỳ":"y","Ỵ":"Y","ỵ":"y","Ỷ":"Y","ỷ":"y","Ỹ":"Y","ỹ":"y","–":"-","‘":"\'","’":"\'","“":"\\\"","”":"\\\"","„":"\\\"","†":"+","•":"*","…":"...","₠":"ecu","₢":"cruzeiro","₣":"french franc","₤":"lira","₥":"mill","₦":"naira","₧":"peseta","₨":"rupee","₩":"won","₪":"new shequel","₫":"dong","€":"euro","₭":"kip","₮":"tugrik","₯":"drachma","₰":"penny","₱":"peso","₲":"guarani","₳":"austral","₴":"hryvnia","₵":"cedi","₸":"kazakhstani tenge","₹":"indian rupee","₺":"turkish lira","₽":"russian ruble","₿":"bitcoin","℠":"sm","™":"tm","∂":"d","∆":"delta","∑":"sum","∞":"infinity","♥":"love","元":"yuan","円":"yen","﷼":"rial","ﻵ":"laa","ﻷ":"laa","ﻹ":"lai","ﻻ":"la"}')
  var locales = JSON.parse('{"bg":{"Й":"Y","Ц":"Ts","Щ":"Sht","Ъ":"A","Ь":"Y","й":"y","ц":"ts","щ":"sht","ъ":"a","ь":"y"},"de":{"Ä":"AE","ä":"ae","Ö":"OE","ö":"oe","Ü":"UE","ü":"ue","ß":"ss","%":"prozent","&":"und","|":"oder","∑":"summe","∞":"unendlich","♥":"liebe"},"es":{"%":"por ciento","&":"y","<":"menor que",">":"mayor que","|":"o","¢":"centavos","£":"libras","¤":"moneda","₣":"francos","∑":"suma","∞":"infinito","♥":"amor"},"fr":{"%":"pourcent","&":"et","<":"plus petit",">":"plus grand","|":"ou","¢":"centime","£":"livre","¤":"devise","₣":"franc","∑":"somme","∞":"infini","♥":"amour"},"pt":{"%":"porcento","&":"e","<":"menor",">":"maior","|":"ou","¢":"centavo","∑":"soma","£":"libra","∞":"infinito","♥":"amor"},"uk":{"И":"Y","и":"y","Й":"Y","й":"y","Ц":"Ts","ц":"ts","Х":"Kh","х":"kh","Щ":"Shch","щ":"shch","Г":"H","г":"h"},"vi":{"Đ":"D","đ":"d"},"da":{"Ø":"OE","ø":"oe","Å":"AA","å":"aa","%":"procent","&":"og","|":"eller","$":"dollar","<":"mindre end",">":"større end"},"nb":{"&":"og","Å":"AA","Æ":"AE","Ø":"OE","å":"aa","æ":"ae","ø":"oe"},"it":{"&":"e"},"nl":{"&":"en"},"sv":{"&":"och","Å":"AA","Ä":"AE","Ö":"OE","å":"aa","ä":"ae","ö":"oe"}}')

  function replace (string, options) {
    if (typeof string !== 'string') {
      throw new Error('slugify: string argument expected')
    }

    options = (typeof options === 'string')
      ? {replacement: options}
      : options || {}

    var locale = locales[options.locale] || {}

    var replacement = options.replacement === undefined ? '-' : options.replacement

    var trim = options.trim === undefined ? true : options.trim

    var slug = string.normalize().split('')
      // replace characters based on charMap
      .reduce(function (result, ch) {
        var appendChar = locale[ch] || charMap[ch] || ch;
        if (appendChar === replacement) {
          appendChar = ' ';
        }
        return result + appendChar
          // remove not allowed characters
          .replace(options.remove || /[^\w\s$*_+~.()'"!\-:@]+/g, '')
      }, '');

    if (options.strict) {
      slug = slug.replace(/[^A-Za-z0-9\s]/g, '');
    }

    if (trim) {
      slug = slug.trim()
    }

    // Replace spaces with replacement character, treating multiple consecutive
    // spaces as a single space.
    slug = slug.replace(/\s+/g, replacement);

    if (options.lower) {
      slug = slug.toLowerCase()
    }

    return slug
  }

  replace.extend = function (customMap) {
    Object.assign(charMap, customMap)
  }

  return replace
}))


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be in strict mode.
(() => {
"use strict";
/*!******************************!*\
  !*** ./src/js/controller.js ***!
  \******************************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _helper_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./helper.js */ "./src/js/helper.js");

_helper_js__WEBPACK_IMPORTED_MODULE_0__.scroller();
_helper_js__WEBPACK_IMPORTED_MODULE_0__.profileRandomColor();
_helper_js__WEBPACK_IMPORTED_MODULE_0__.status_update();
_helper_js__WEBPACK_IMPORTED_MODULE_0__.closeDropdown();

// helper.paginationBtnClick()

// function readCookie(name) {
//     let nameEQ = name + "=";
//     let ca = document.cookie.split(';');
//     for (let i = 0; i < ca.length; i++) {
//         let c = ca[i];
//         while (c.charAt(0) == ' ') c = c.substring(1, c.length);
//         if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
//     }
//     return null;
// }

// const csrftoken = readCookie('csrftoken');
// const slugify = require('slugify')

// let test
// const status_update = async function () {
//     await fetch('http://127.0.0.1:8000/api/get_status/?format=json').then(function (response) {
//         return response.json()
//     }).then(function (data) {

//         const ne1w = data.map(function (status) {

//             let html = `<a data-status-value="${status.status_name}"class="change-status--link" href="#">
//                             <div class="display-status-${slugify(status.status_name).toLowerCase()}">
//                                 <div class='display-status-text'>${status.status_name}</div>
//                             </div>
//                         </a>`
//             return html
//         }
//         )
//         test = ne1w
//     })

// }

// const statusEL = document.querySelectorAll('.display-ticket-status');
// statusEL.forEach(function (el) {
//     el.addEventListener('click', function (e) {
//         e.preventDefault();
//         el.insertAdjacentHTML('beforebegin', `<div class="change-status--container">` + test.join("") + `</div>`
//         )
//         const status_value = dropdownBtnClick(el)

//     }

//     )

// }

// )

// function dropdownBtnClick(status_element) {
//     const dropdownBtn = document.querySelectorAll(".change-status--link")
//     dropdownBtn.forEach(function (el) {
//         el.addEventListener('click', function (e) {
//             e.preventDefault();
//             const el_id = el.closest('.ticket-main-row')

//             fetch("http://127.0.0.1:8000/api/post_status/", {

//                 // Adding method type
//                 method: "POST",

//                 // Adding body or contents to send
//                 body: JSON.stringify({
//                     id: el_id.dataset.id,
//                     status: el.dataset.statusValue
//                 }),

//                 // Adding headers to the request
//                 headers: {
//                     "Content-type": "application/json; charset=UTF-8",
//                     "X-CSRFToken": csrftoken
//                 }
//             })

//                 // Converting to JSON
//                 .then(response => response.json())

//                 // Displaying results to console
//                 .then(function (json) {
//                     console.log(json)
//                     console.log(status_element)
//                     status_element.firstElementChild.classList = `display-status-${slugify(el.dataset.statusValue).toLowerCase()}`
//                     el.closest('.change-status--container').remove()
//                     status_element.querySelector('.display-status-text').innerHTML = el.dataset.statusValue
//                 });

//         })
//     })

// }

// status_update()
})();

/******/ })()
;
//# sourceMappingURL=index.js.map