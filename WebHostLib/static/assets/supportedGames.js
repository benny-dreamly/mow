window.addEventListener('load', () => {
  // Add toggle listener to all elements with .collapse-toggle
  const toggleButtons = document.querySelectorAll('details');

  // Favorites functionality
  const FAVORITES_STORAGE_KEY = 'mwgg_favorite_games';
  const favoritesSection = document.getElementById('favorites-section');
  const favoritesList = document.getElementById('favorites-list');
  let favoriteGames = new Set();
  let originalElements = new Map(); // Store original elements for cloning

  // Load favorites from localStorage
  function loadFavorites() {
    try {
      const stored = localStorage.getItem(FAVORITES_STORAGE_KEY);
      if (stored) {
        favoriteGames = new Set(JSON.parse(stored));
      }
    } catch (e) {
      console.warn('Failed to load favorites from localStorage:', e);
    }
  }

  // Save favorites to localStorage
  function saveFavorites() {
    try {
      localStorage.setItem(FAVORITES_STORAGE_KEY, JSON.stringify([...favoriteGames]));
    } catch (e) {
      console.warn('Failed to save favorites to localStorage:', e);
    }
  }

  // Update star icon appearance
  function updateStarIcon(starIcon, isFavorited) {
    if (isFavorited) {
      starIcon.classList.add('favorited');
      starIcon.title = 'Remove from favorites';
    } else {
      starIcon.classList.remove('favorited');
      starIcon.title = 'Add to favorites';
    }
  }

  // Toggle favorite status
  function toggleFavorite(gameName) {
    if (favoriteGames.has(gameName)) {
      favoriteGames.delete(gameName);
    } else {
      favoriteGames.add(gameName);
    }
    saveFavorites();
    updateFavoritesSection();
    updateMainListVisibility();
  }

  // Update the favorites section
  function updateFavoritesSection() {
    if (favoriteGames.size === 0) {
      favoritesSection.style.display = 'none';
      // Update star icons in the main list when favorites section is hidden
      document.querySelectorAll('.star-icon').forEach(starIcon => {
        const gameName = starIcon.getAttribute('data-game');
        if (gameName) {
          updateStarIcon(starIcon, favoriteGames.has(gameName));
        }
      });
      return;
    }

    favoritesSection.style.display = 'block';
    favoritesList.innerHTML = '';

    favoriteGames.forEach(gameName => {
      // Get the original element from our stored map
      const originalElement = originalElements.get(gameName);
      if (!originalElement) return;

      const clone = originalElement.cloneNode(true);
      clone.classList.add('favorite-game-item');
      
      // Update the star icon in the clone
      const starIcon = clone.querySelector('.star-icon');
      if (starIcon) {
        updateStarIcon(starIcon, true);
        starIcon.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          toggleFavorite(gameName);
        });
      }

      favoritesList.appendChild(clone);
    });

    // Update star icons in the main list
    document.querySelectorAll('.star-icon').forEach(starIcon => {
      const gameName = starIcon.getAttribute('data-game');
      if (gameName) {
        updateStarIcon(starIcon, favoriteGames.has(gameName));
      }
    });
  }

  // Update main list visibility to hide favorited games
  function updateMainListVisibility() {
    // Only target details in the main list, not in the favorites section
    document.querySelectorAll('#games > details').forEach(detail => {
      const gameName = detail.getAttribute('data-game');
      if (gameName && favoriteGames.has(gameName)) {
        detail.style.display = 'none';
      } else {
        detail.style.display = null;
      }
    });
  }

  // Store original elements for cloning
  function storeOriginalElements() {
    document.querySelectorAll('details').forEach(detail => {
      const gameName = detail.getAttribute('data-game');
      if (gameName) {
        originalElements.set(gameName, detail.cloneNode(true));
      }
    });
  }

  // Add click handlers to all star icons
  function initializeStarIcons() {
    document.querySelectorAll('.star-icon').forEach(starIcon => {
      const gameName = starIcon.getAttribute('data-game');
      if (!gameName) return;

      updateStarIcon(starIcon, favoriteGames.has(gameName));
      
      starIcon.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        toggleFavorite(gameName);
      });
    });
  }

  // Initialize favorites
  loadFavorites();
  storeOriginalElements();
  initializeStarIcons();
  updateFavoritesSection();
  updateMainListVisibility();

  // Handle game filter input
  const gameSearch = document.getElementById('game-search');
  gameSearch.value = '';
  gameSearch.addEventListener('input', (evt) => {
    const searchTerm = evt.target.value.toLowerCase().trim();
    
    if (!searchTerm) {
      // If input is empty, display all games as collapsed
      toggleButtons.forEach((header) => {
        header.style.display = null;
        header.removeAttribute('open');
      });
      
      // Also restore all favorites to visible
      const favoriteItems = favoritesList.querySelectorAll('.favorite-game-item');
      favoriteItems.forEach(item => {
        item.style.display = null;
        item.removeAttribute('open');
      });
      return;
    }

    // Loop over all the games
    toggleButtons.forEach((header) => {
      // If the game name includes the search string, display the game. If not, hide it
      if (header.getAttribute('data-game').toLowerCase().includes(searchTerm) || header.getAttribute('data-display-name').toLowerCase().includes(searchTerm)) {
        header.style.display = null;
        header.setAttribute('open', '1');
      } else {
        header.style.display = 'none';
        header.removeAttribute('open');
      }
    });

    // Also filter favorites section
    const favoriteItems = favoritesList.querySelectorAll('.favorite-game-item');
    favoriteItems.forEach(item => {
      const gameName = item.getAttribute('data-game').toLowerCase();
      const displayName = item.getAttribute('data-display-name').toLowerCase();
      
      if (gameName.includes(searchTerm) || displayName.includes(searchTerm)) {
        item.style.display = null;
        item.setAttribute('open', '1');
      } else {
        item.style.display = 'none';
        item.removeAttribute('open');
      }
    });
  });

  document.getElementById('expand-all').addEventListener('click', expandAll);
  document.getElementById('collapse-all').addEventListener('click', collapseAll);

  const COOKIE_NAME = 'show_hidden_games';

  function setCookie(name, value, days = 365) {
    const expires = new Date(
      Date.now() + days * 24 * 60 * 60 * 1000
    ).toUTCString();
    document.cookie = `${name}=${value};expires=${expires};path=/`;
  }

  function getCookie(name) {
    return document.cookie
      .split('; ')
      .find((row) => row.startsWith(name + '='))
      ?.split('=')[1];
  }

  function updateNSFWVisibility() {
    const show = getCookie(COOKIE_NAME) === 'true';
    document.querySelectorAll('details[data-nsfw="true"]').forEach((el) => {
      el.style.display = show ? '' : 'none';
    });
    document.getElementById('toggle-nsfw').textContent = show
      ? 'Hide NSFW games'
      : 'Show NSFW games';
  }

  document.getElementById('toggle-nsfw').addEventListener('click', (e) => {
    e.preventDefault();
    const currently = getCookie(COOKIE_NAME) === 'true';
    setCookie(COOKIE_NAME, !currently);
    updateNSFWVisibility();
  });

  updateNSFWVisibility();
});

const expandAll = () => {
  document.querySelectorAll('details').forEach((detail) => {
    detail.setAttribute('open', '1');
  });
};

const collapseAll = () => {
  document.querySelectorAll('details').forEach((detail) => {
    detail.removeAttribute('open');
  });
};
