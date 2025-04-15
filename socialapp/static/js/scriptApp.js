document.getElementById('post-form').addEventListener('submit', function (e) {
  e.preventDefault();
  const content = document.getElementById('post-content').value;

  const post = document.createElement('div');
  post.classList.add('post');
  post.dataset.liked = 'false';
  post.dataset.disliked = 'false';
  post.innerHTML = `
    <p>${content}</p>
    <div class="post-actions">
      <button onclick="like(this)">👍 Curtir <span class="like-count">0</span></button>
      <button onclick="dislike(this)">👎 Descurtir <span class="dislike-count">0</span></button>
      <button onclick="comment(this)">💬 Comentar</button>
      <button onclick="share(this)">🔁 Compartilhar</button>
    </div>
  `;

  document.getElementById('posts').prepend(post);
  document.getElementById('post-content').value = '';
});

function like(button) {
  const post = button.closest('.post');
  const liked = post.dataset.liked === 'true';
  const disliked = post.dataset.disliked === 'true';

  if (!liked && !disliked) {
    const likeCountSpan = button.querySelector('.like-count');
    let count = parseInt(likeCountSpan.innerText);
    likeCountSpan.innerText = count + 1;
    post.dataset.liked = 'true';
  }
}

function dislike(button) {
  const post = button.closest('.post');
  const liked = post.dataset.liked === 'true';
  const disliked = post.dataset.disliked === 'true';

  if (!disliked && !liked) {
    const dislikeCountSpan = button.querySelector('.dislike-count');
    let count = parseInt(dislikeCountSpan.innerText);
    dislikeCountSpan.innerText = count + 1;
    post.dataset.disliked = 'true';
  }
}

function comment(button) {
  const comment = prompt("Digite seu comentário:");
  if (comment) {
    const post = button.closest('.post');
    const commentEl = document.createElement('p');
    commentEl.textContent = `💬 ${comment}`;
    commentEl.style.marginTop = '10px';
    post.appendChild(commentEl);
  }
}

function share(button) {
  // Aqui poderia ter integração com redes sociais ou copiar link
  console.log("Post compartilhado!");
}
