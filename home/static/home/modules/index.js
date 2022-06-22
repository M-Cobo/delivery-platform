import {
    displayNearbyStores,
    setStoreNavigation,
} from './stores.js';

import {
    displayNearbyWishlists,
    displayMyRequests,
    displayMyTrips,
    createWishlist,
    updateWishlistStatus,
} from './wishlists.js';

import {
    addMap,
} from './map.js';

export const USERNAME = document.body.getAttribute("data-username");

let MAP = {};

MAP = addMap();

L.Control.geocoder().on('markgeocode', (data) => {
    Promise.all([
        displayNearbyStores(MAP, data.geocode.center.lat, data.geocode.center.lng),
        displayNearbyWishlists(data.geocode.center.lat, data.geocode.center.lng),
        displayMyRequests(data.geocode.center.lat, data.geocode.center.lng),
        displayMyTrips(data.geocode.center.lat, data.geocode.center.lng)
    ]).then(([storesGeoJson]) => {
        setStoreNavigation(MAP, storesGeoJson);
    });
  }).addTo(MAP);

  document.getElementById('add-wishlist').onclick = function(e) {
      createWishlist();
  }