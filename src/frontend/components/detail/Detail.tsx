import React from 'react';
import PokemonDetailDTO from '../../context/dto/PokemonDetailDTO';

const Detail = (props: PokemonDetailDTO) => {
  console.log(props);
  return (
    <div>
      <h1>Tera Types:</h1>
      {props.pokemon.tera_type.map((type, index) => (
        <div key={index}>
          <p>Name: {type.name}</p>
          <p>Usage: {type.usage + "%"}</p>
          <br></br>
        </div>
      ))}

      <h1>Abilities:</h1>
      {props.pokemon.ability.map((ability, index) => (
        <div key={index}>
          <p>Name: {ability.name}</p>
          <p>Usage: {ability.usage + "%"}</p>
          <br></br>
        </div>
      ))}

      <h1>Items:</h1>
      {props.pokemon.item.map((item, index) => (
        <div key={index}>
          <p>Name: {item.name}</p>
          <p>Usage: {item.usage + "%"}</p>
          <br></br>
        </div>
      ))}

      <h1>Moves:</h1>
      {props.pokemon.moves.map((move, index) => (
        <div key={index}>
          <p>Name: {move.name}</p>
          <p>Usage: {move.usage + "%"}</p>
          <br></br>
        </div>
      ))}
    </div>
  );
};

export default Detail;
