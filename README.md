# Roberto Rossini — Portfolio Backend Developer

Portfolio pessoal desenvolvido em **HTML/CSS/JS puro (zero frameworks)**, com foco em sistemas de baixo nível, Rust, Spring Boot e game development. Deploy contínuo no Vercel.

## 🖥️ Screenshots

| Desktop (1200px) | Tablet (768px) | Mobile (390px) |
|:----------------:|:--------------:|:--------------:|
| ![Desktop](screenshots/desktop-1200px.png) | ![Tablet](screenshots/tablet-768px.png) | ![Mobile](screenshots/mobile-390px.png) |

## 🛠️ Stack

- **Frontend:** HTML5, CSS3 (custom properties, Grid/Flexbox), Vanilla JS (ES6+)
- **Estilo:** Design system "cyber-metal" — tokens CSS, scanlines, tipografia híbrida (Orbitron + JetBrains Mono), sombras sólidas, zero border-radius
- **i18n:** PT/EN com troca dinâmica sem reload
- **Deploy:** Vercel (static hosting, auto-deploy on push to main)
- **Ferramentas:** Playwright (screenshots), GitHub Actions (opcional)

## 🔗 Site em produção

https://port-rossini-roberto.vercel.app

## 🚀 Como rodar localmente

```bash
# Clone
git clone https://github.com/rossiniroberto52/portf-lio.git
cd portf-lio

# Servidor estático simples (qualquer um funciona)
npx serve .          # ou: python3 -m http.server 8080
# Abre em http://localhost:3000 (serve) ou http://localhost:8080 (python)
```

> Não há build step, bundler ou dependências de runtime. Abra `index.html` diretamente no navegador se preferir.

## 📂 Estrutura

```
├── index.html           # Single-page application (PT/EN)
├── css/style.css        # Design system + layout responsivo
├── js/
│   ├── main.js          # Inicialização, i18n, scroll-reveal
│   └── github.js        # Lista estática de repos (PT/EN overrides)
├── assets/imgs/         # Imagens locais (certificados, og-preview)
├── screenshots/         # Playwright screenshots (README)
├── cyber-ux.txt         # Design system reference (cyber-metal aesthetic)
└── LINKEDIN_POSTS.md    # Posts do LinkedIn referenciados no portfolio
```

## 🎯 Projetos em destaque

| Projeto | Stack | Descrição |
|---------|-------|-----------|
| **LLM Model by Scratch** | Rust, Candle, safetensors | LLM from scratch (tokenizer, attention, sampling) |
| **Quartz** | C, WASM | Execution engine / runtime experimental |
| **Veloce-Rent-a-Car (CarRental API)** | Java 17, Spring Boot 3, PostgreSQL, JWT | REST API completa com auth, reservas, pagamentos |
| **Plataforma EJUNICAP** | FastAPI, PostgreSQL, AsyncIO | Sistema interno da Empresa Júnior (demandas, clientes, projetos) |
| **Agente Telegram EJ** | Python, RAG, Chroma, Ollama | Bot com busca vetorial + LLM local para FAQ da EJ |
| **Custom 2D Game Engine** | C++17, SDL2, ECS | Engine 2D from scratch: game loop, manual memory, sprite rendering |
| **Don't let it fall (GGJ 2026)** | Unity, C# | Vencedor "Melhor Visual" e "Melhor Jogo" na Poli UPE |
| **Audity-sim** | Python, Taichi Lang | Simulador acústico 2D GPU-accelerated |

## 📜 Certificados

- **Winter Game Jam 2026** — Tema: VaporWave (Global Game Jam)
- **Efetivação EJUNICAP** — Membro efetivo da Empresa Júnior

## 📄 Licença

MIT — use como referência, estude, adapte. Créditos apreciados.