const busca = document.getElementById('busca');
busca.addEventListener('input', function () {
    const texto = busca.value.toLowerCase();
    let visiveis = 0;
    document.querySelectorAll('#lista-equipes .card').forEach(function (card) {
        const nome = card.querySelector('h3').textContent.toLowerCase();
        card.hidden = !nome.includes(texto);
        if (!card.hidden) visiveis++;
    });
    document.getElementById('sem-resultado').hidden = visiveis > 0;
});
