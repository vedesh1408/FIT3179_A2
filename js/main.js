var specVis1 = "./js/world_happiness_index-1.vg.json";
var specVis2 = "./js/world_happiness_index-2.vg.json";
var specVis3 = "./js/world_happiness_index-3.vg.json";
var specVis4 = "./js/world_happiness_index-4.vg.json";
var specVis5 = "./js/world_happiness_index-5.vg.json";


vegaEmbed('#world_happiness_index-1', specVis1, {
    "actions": false
});

vegaEmbed('#world_happiness_index-2', specVis2, {
    "actions": false
}).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

//vegaEmbed('#world_happiness_index-3', specVis3, { "actions": false });

vegaEmbed('#world_happiness_index-3', specVis3, {
    "actions": false
}).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

vegaEmbed('#world_happiness_index-4', specVis4, { "actions": false }).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

vegaEmbed('#world_happiness_index-5', specVis5, { "actions": false }).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);