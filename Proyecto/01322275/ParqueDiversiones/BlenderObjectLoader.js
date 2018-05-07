function blenderObjectLoader(pathToMaterial, pathToObject){
  var myObject = new THREE.Mesh();
  var onProgress = function ( xhr ) {
      if ( xhr.lengthComputable ) {
          var percentComplete = xhr.loaded / xhr.total * 100;
          console.log( Math.round(percentComplete, 2) + '% downloaded' );
      }
  };

  var onError = function ( xhr ) { };
  THREE.Loader.Handlers.add( /\.dds$/i, new THREE.DDSLoader() );

  var mtlLoader = new THREE.MTLLoader();

  //LOAD
  var obj;
  mtlLoader.load( pathToMaterial, function( materials ) {
      materials.preload();
      var objLoader = new THREE.OBJLoader();
      objLoader.setMaterials( materials );
      objLoader.load( pathToObject, function ( object ) {
          obj = object;
          object.traverse( function ( child )
          {
              if ( child instanceof THREE.Mesh )
              {
                  child.material = redMaterial;
              }
          } );
          myObject.add(obj);
      }, onProgress, onError );
  });

  return myObject;
}
