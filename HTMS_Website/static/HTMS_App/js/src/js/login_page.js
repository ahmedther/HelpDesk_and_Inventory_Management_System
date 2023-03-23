const deleteErrorFunc = function () {
    const errorEl = document.querySelector('.error');
    setTimeout(() => errorEl.remove(), 12 * 1000)

}
const scroller = function () {
    const progress = document.querySelector(".progressbar");
    const totalHeight = document.body.scrollHeight - window.innerHeight;
    window.onscroll = function () {
        const progressHeight = (window.pageYOffset / totalHeight) * 100;
        progress.style.height = progressHeight + "%";
    };
};

deleteErrorFunc()
scroller()