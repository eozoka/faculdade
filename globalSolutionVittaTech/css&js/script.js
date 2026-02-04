document.querySelectorAll('.faq-question').forEach(question => {
  question.addEventListener('click', () => {
    const answer = question.nextElementSibling;
    answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
    question.classList.toggle('active');
  });
});

const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!email || !password) {
      alert('Por favor, preencha todos os campos.');
      return;
    }

    alert(`Bem-vindo, ${email}!`);
    loginForm.reset();
  });
}

document.querySelectorAll('.card a').forEach(link => {
  link.addEventListener('mouseenter', () => {
    link.style.color = '#00ff7f';
    link.style.transform = 'scale(1.1)';
  });
  link.addEventListener('mouseleave', () => {
    link.style.color = '#fff';
    link.style.transform = 'scale(1)';
  });
});

document.querySelectorAll('.course-card').forEach(card => {
  card.addEventListener('click', () => {
    const course = card.getAttribute('data-course');

    switch(course) {
      case 'programacao':
        window.location.href = 'programacao.html';
        break;
      case 'ia':
        window.location.href = 'ia.html';
        break;
      case 'softskills':
        window.location.href = 'softskills.html';
        break;
    }
  });
});
