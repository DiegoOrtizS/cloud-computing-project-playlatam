/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/detail/[param]&[a]";
exports.ids = ["pages/detail/[param]&[a]"];
exports.modules = {

/***/ "./pages/detail/[param]&[a].tsx":
/*!**************************************!*\
  !*** ./pages/detail/[param]&[a].tsx ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"getServerSideProps\": () => (/* binding */ getServerSideProps)\n/* harmony export */ });\n/* harmony import */ var bootstrap_dist_css_bootstrap_min_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! bootstrap/dist/css/bootstrap.min.css */ \"./node_modules/bootstrap/dist/css/bootstrap.min.css\");\n/* harmony import */ var bootstrap_dist_css_bootstrap_min_css__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(bootstrap_dist_css_bootstrap_min_css__WEBPACK_IMPORTED_MODULE_0__);\n\nconst getServerSideProps = async (ctx)=>{\n    try {\n        const { tournament_id , pokemon_name  } = ctx.query;\n        console.log(tournament_id, pokemon_name);\n        return {\n            props: {\n                tournament_id: tournament_id,\n                pokemon_name: \"a\"\n            }\n        };\n    } catch  {\n        return {\n            notFound: true\n        };\n    }\n};\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9kZXRhaWwvW3BhcmFtXSZbYV0udHN4LmpzIiwibWFwcGluZ3MiOiI7Ozs7OztBQUc4QztBQUV2QyxNQUFNQSxxQkFBcUQsT0FDaEVDLE1BQ0c7SUFDSCxJQUFJO1FBQ0YsTUFBTSxFQUFFQyxjQUFhLEVBQUVDLGFBQVksRUFBRSxHQUFHRixJQUFJRyxLQUFLO1FBQ2pEQyxRQUFRQyxHQUFHLENBQUNKLGVBQWVDO1FBRTNCLE9BQU87WUFDTEksT0FBTztnQkFDTEwsZUFBZUE7Z0JBQ2ZDLGNBQWM7WUFDaEI7UUFDRjtJQUNGLEVBQUUsT0FBTTtRQUNOLE9BQU87WUFDTEssVUFBVSxJQUFJO1FBQ2hCO0lBQ0Y7QUFDRixFQUFFIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vcmVjbGFtYWxvLWZyb250ZW5kLy4vcGFnZXMvZGV0YWlsL1twYXJhbV0mW2FdLnRzeD8zNGU4Il0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IEdldFNlcnZlclNpZGVQcm9wcywgR2V0U2VydmVyU2lkZVByb3BzQ29udGV4dCB9IGZyb20gXCJuZXh0XCI7XHJcbmltcG9ydCBKU1ggZnJvbSBcIm5leHRcIjtcclxuaW1wb3J0IFBva2Vtb25EVE8gZnJvbSBcImNvbnRleHQvZHRvL1Bva2Vtb25EVE9cIjtcclxuaW1wb3J0IFwiYm9vdHN0cmFwL2Rpc3QvY3NzL2Jvb3RzdHJhcC5taW4uY3NzXCI7XHJcblxyXG5leHBvcnQgY29uc3QgZ2V0U2VydmVyU2lkZVByb3BzOiBHZXRTZXJ2ZXJTaWRlUHJvcHM8UG9rZW1vbkRUTz4gPSBhc3luYyAoXHJcbiAgY3R4OiBHZXRTZXJ2ZXJTaWRlUHJvcHNDb250ZXh0XHJcbikgPT4ge1xyXG4gIHRyeSB7XHJcbiAgICBjb25zdCB7IHRvdXJuYW1lbnRfaWQsIHBva2Vtb25fbmFtZSB9ID0gY3R4LnF1ZXJ5O1xyXG4gICAgY29uc29sZS5sb2codG91cm5hbWVudF9pZCwgcG9rZW1vbl9uYW1lKTtcclxuICAgIFxyXG4gICAgcmV0dXJuIHtcclxuICAgICAgcHJvcHM6IHtcclxuICAgICAgICB0b3VybmFtZW50X2lkOiB0b3VybmFtZW50X2lkLFxyXG4gICAgICAgIHBva2Vtb25fbmFtZTogXCJhXCIsXHJcbiAgICAgIH0sXHJcbiAgICB9O1xyXG4gIH0gY2F0Y2gge1xyXG4gICAgcmV0dXJuIHtcclxuICAgICAgbm90Rm91bmQ6IHRydWUsXHJcbiAgICB9O1xyXG4gIH1cclxufTtcclxuIl0sIm5hbWVzIjpbImdldFNlcnZlclNpZGVQcm9wcyIsImN0eCIsInRvdXJuYW1lbnRfaWQiLCJwb2tlbW9uX25hbWUiLCJxdWVyeSIsImNvbnNvbGUiLCJsb2ciLCJwcm9wcyIsIm5vdEZvdW5kIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./pages/detail/[param]&[a].tsx\n");

/***/ }),

/***/ "./node_modules/bootstrap/dist/css/bootstrap.min.css":
/*!***********************************************************!*\
  !*** ./node_modules/bootstrap/dist/css/bootstrap.min.css ***!
  \***********************************************************/
/***/ (() => {



/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("./pages/detail/[param]&[a].tsx"));
module.exports = __webpack_exports__;

})();