import {
    updateSelectedStore,
} from './stores.js';

/**
 * @typedef {import('./api').Store} Store
 */

/**
 * Stores GeoJSON Feature object
 * @typedef {Object} StoreFeatureObject
 * @property {'Feature'} type
 * @property {{type: 'Point', coordinates: [number, number] }} geometry
 * @property {Store} properties
 */

/**
 * Stores GeoJSON FeatureCollection
 * @typedef {Object} StoresGeoJSON
 * @property {'FeatureCollection'} type
 * @property {StoreFeatureObject[]} features
 */

/**
 * Create a new mapbox map instance
 * @return {Object} Map
 */
export function addMap() {
    const map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    return map;
}

/**
 * Converts array of stores to GeoJSON format
 * @param {Store[]} stores
 * @return {StoresGeoJSON} Stores in GeoJSON
 */
export function convertToGeoJson(stores) {return {
    type: "FeatureCollection",
    features: stores.map(store => {
        return {
            type: "Feature",
            geometry: {
                type: 'Point',
                coordinates: [store.longitude, store.latitude]
            },
            properties: {
                id: store.id,
                name: store.name,
                address: store.address,
                phone: store.phone,
                distance: store.distance,
                rating: store.rating,
            }
        }
    })
}}

/**
 * Display stores on map
 * @param {Object} map
 * @param {StoresGeoJSON} storesGeoJson
 */
export function plotStoresOnMap(map, storesGeoJson) {
    var storeIcon = L.divIcon({
        className: 'store',
        iconSize: [30, 30]
    });

    for(let store of storesGeoJson.features) {
        // create a HTML element for each feature  
        let el = document.createElement('div');  
        el.className = 'store';  
        el.title = `${store.properties.name}<br>` +  
        `approximately ${store.properties.distance.toFixed(2)} km away<br>` +  
        `Address: ${store.properties.address || "N/A"}<br>` +  
        `Phone: ${store.properties.phone || "N/A"}<br>` +  
        `Rating: ${store.properties.rating || "N/A"}`; 
        // make a marker for each feature and add to the map
        L.geoJSON(store, {
            pointToLayer: function (feature, latlgn) {
                return L.marker(latlgn, {icon: storeIcon}).on('click', function(e) {
                    updateSelectedStore(store.properties.id);
                });
            }
        }).addTo(map).bindTooltip(el.title);
    }
}

/**
 * Zoom in-to a specific point on a map
 * @param {Object} map
 * @param {StoreFeatureObject} point
 */
export function flyToStore(map, point) {

}

/**
 * Display store info on the map using a popup
 * @param {Object} map
 * @param {StoreFeatureObject} point
 */
export function displayStoreDetails(map, point) {
    
}
