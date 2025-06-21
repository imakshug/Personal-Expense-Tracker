let userId = localStorage.getItem('userId');
  if (!userId) {
    userId = crypto.randomUUID();
    localStorage.setItem('userId', userId);
  }

  const toggleButton = document.getElementById('themeToggle');

  function setTheme(mode) {
    document.body.classList.remove('light', 'dark');
    document.body.classList.add(mode);
    localStorage.setItem('theme', mode);
    toggleButton.textContent = mode === 'dark' ? '☀️' : '🌙';
  }

  // Load saved or system theme
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  setTheme(saved || (prefersDark ? 'dark' : 'light'));

  // Toggle
  toggleButton.addEventListener('click', () => {
    const current = document.body.classList.contains('dark') ? 'dark' : 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    setTheme(next);
  });

    function loadExpenses(filters = {}) {
    let url = '/expenses';
    const params = new URLSearchParams(filters);
    if ([...params].length) {
      url = '/filter?' + params.toString();
    }

    fetch(url)
      .then(res => res.json())
      .then(data => {
        const tbody = document.getElementById('expensesBody');
        tbody.innerHTML = '';

        if (data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5">No expenses recorded.</td></tr>';
          return;
        }

        // ✅ SORT by date DESC (newest first)
        data.sort((a, b) => new Date(b.date) - new Date(a.date));

        data.forEach(exp => {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td>${exp.date || '-'}</td>
            <td>${exp.category || '-'}</td>
            <td>₹ ${parseFloat(exp.amount || 0).toFixed(2)}</td>
            <td>${exp.description || '-'}</td>
            <td><button onclick="deleteExpense('${exp.date}', '${exp.category}', '${exp.amount}', '${exp.description}')">Delete</button></td>
          `;
          tbody.appendChild(row);
        });
      })
      .catch(() => {
        document.getElementById('expensesBody').innerHTML = '<tr><td colspan="5">Error loading expenses.</td></tr>';
      });
  }

  document.getElementById('expenseForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const data = {
      date: document.getElementById('date').value,
      category: document.getElementById('category').value,
      amount: document.getElementById('amount').value,
      description: document.getElementById('description').value
    };

    fetch('/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(() => {
        this.reset();
        loadExpenses();
      });
  });

  document.getElementById('filterForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const filters = {};
  const category = document.getElementById('filterCategory').value.trim();
  const startDate = document.getElementById('filterStart').value;

  if (category) filters.category = category;
  if (startDate) filters.start_date = startDate;

  loadExpenses(filters);
});
  // Function to delete an expense
  // This function sends a request to the server to delete an expense

  function deleteExpense(date, category, amount, description) {
    fetch('/delete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ date, category, amount, description })
    })
      .then(res => res.json())
      .then(() => {
        loadExpenses();
      });
  }

  window.onload = () => loadExpenses();