document.addEventListener('DOMContentLoaded', () => {
    const incomeTab = document.getElementById('income-tab');
    const expenseTab = document.getElementById('expense-tab');
    const incomeForm = document.getElementById('income-form');
    const expenseForm = document.getElementById('expense-form');

    incomeTab.addEventListener('click', () => {
        incomeTab.classList.add('active');
        expenseTab.classList.remove('active');
        incomeForm.classList.add('active');
        expenseForm.classList.remove('active');
    });

    expenseTab.addEventListener('click', () => {
        expenseTab.classList.add('active');
        incomeTab.classList.remove('active');
        expenseForm.classList.add('active');
        incomeForm.classList.remove('active');
    });
});


