console.log('detail 페이지입니다.')

document.addEventListener("DOMContentLoaded", function () {
    // 숫자를 3자리마다 쉼표로 포맷하는 함수
    const formatNumber = (num) => num.toLocaleString('en-US');

    // 제작비 요소와 수익 요소 가져오기
    const budgetElement = document.querySelector(".budget:nth-of-type(1)");
    const revenueElement = document.querySelector(".budget:nth-of-type(2)");

    // 제작비와 수익 텍스트에서 숫자만 추출
    const budgetText = budgetElement.textContent.match(/\d+/g)?.join("") || "0";
    const revenueText = revenueElement.textContent.match(/\d+/g)?.join("") || "0";

    // 숫자로 변환
    const budget = parseInt(budgetText, 10);
    const revenue = parseInt(revenueText, 10);

    // NaN이 아닌 경우에만 포맷팅
    if (!isNaN(budget)) {
        budgetElement.textContent = `제작비: ${formatNumber(budget)}`;
    }
    if (!isNaN(revenue)) {
        revenueElement.textContent = `수익: ${formatNumber(revenue)}`;
    }
});