# Crypto News Scraper 🚀

Un agrégateur d'actualités crypto qui rassemble les dernières news de différentes sources financières majeures.

## 📋 Fonctionnalités

- Agrégation d'actualités crypto en temps réel
- Filtrage par date
- Sources multiples (Coindesk, CNBC, Reuters, etc.)
- Interface utilisateur moderne et responsive
- Mise à jour automatique des actualités

## 🛠 Prérequis

- Python 3.10 ou supérieur
- Node.js 16 ou supérieur
- Chrome/Chromium
- Git

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone <votre-repo>
cd crypto-news-scraper
```

### 2. Backend

```bash
cd backend

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Sur Windows :
.venv\Scripts\activate
# Sur macOS/Linux :
source .venv/bin/activate

# Installer les dépendances et configurer
python setup.py
```

### 3. Frontend

```bash
cd frontend

# Installer les dépendances
npm install

# Créer le fichier .env
echo "VITE_API_URL=http://localhost:8000" > .env
```

## 🎯 Lancement

### Backend

```bash
cd backend
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows
uvicorn main:app --reload
```

Le backend sera disponible sur : http://localhost:8000

### Frontend

```bash
cd frontend
npm run dev
```

Le frontend sera disponible sur : http://localhost:5173

## 🗂 Structure du projet

```
crypto-news-scraper/
├── backend/
│   ├── api/              # Routes FastAPI
│   ├── scrapers/         # Scrapers pour chaque site
│   ├── requirements.txt  # Dépendances Python
│   ├── setup.py         # Script d'installation
│   └── cleanup.py       # Utilitaire de nettoyage
└── frontend/
    ├── src/
    │   ├── components/   # Composants React
    │   └── services/     # Services API
    ├── package.json
    └── .env
```

## 🔧 Dépannage

### Erreurs courantes

1. **Erreur de Chrome/Playwright**

   ```bash
   cd backend
   python -m playwright install chromium
   ```

2. **Le backend ne démarre pas**

   - Vérifiez que tous les ports sont disponibles
   - Nettoyez les données temporaires :

   ```bash
   cd backend
   python cleanup.py
   ```

3. **Le frontend ne se connecte pas au backend**
   - Vérifiez que le backend est bien lancé
   - Vérifiez le fichier `.env` dans le dossier frontend

## 🔒 Versions des dépendances

### Backend

- FastAPI: 0.68.1
- Uvicorn: 0.15.0
- Playwright: 1.42.0
- BeautifulSoup4: 4.9.3
- Python-dateutil: 2.8.2

### Frontend

- React: 18.2.0
- Material-UI: 5.11.12
- Axios: 1.3.4
- Date-fns: 2.29.3
- Vite: 4.2.0

## 📝 Sources d'actualités

- Coindesk
- CNBC
- Reuters
- MarketWatch
- Bloomberg
- Financial Times
- Wall Street Journal
- New York Times

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📜 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## 📞 Support

Pour toute question ou problème :

1. Consultez la section Dépannage ci-dessus
2. Ouvrez une issue sur GitHub
3. Vérifiez les logs du backend et du frontend
