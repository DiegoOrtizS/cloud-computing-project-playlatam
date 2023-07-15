import React, { ReactElement, useRef, useState } from "react";
import { TextField, InputAdornment, Button } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import styles from "./Search.module.css";
import { getPokemonByTournamentId } from "../../use_cases/pokemon/getPokemonByTournamentId";
import PokemonDTO from "../../context/dto/PokemonDTO";
import { useRouter } from 'next/router';
import Detail from "../detail/Detail";
import { Route } from "react-router-dom";
import { getTournament } from "../../use_cases/tournament/getTournament";
import TournamentDTO from "../../context/dto/TournamentDTO";

export const Search: React.FC = (): ReactElement => {
  const searchInputRef = useRef<HTMLInputElement>(null);
  const [searchValue, setSearchValue] = useState("");
  const [searchResults, setSearchResults] = useState<PokemonDTO[]>([]);
  const [tournament, setTournament] = useState<TournamentDTO | null>(null);
  const router = useRouter();

  const handleSearch = async () => {
    const responsePromise = getTournament(searchValue);
    const pokemonPromise = getPokemonByTournamentId(searchValue);
    const [response, pokemon] = await Promise.all([responsePromise, pokemonPromise]);
    setTournament(response.data);
    setSearchResults(pokemon.data.pokemon);
  };

  const handleKeyDown = async (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      event.preventDefault();
      searchInputRef.current?.blur();
      await handleSearch();
    }
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchValue(event.target.value);
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        {tournament && (
          <div>
            <div key={tournament.category} className={styles.result}>
              {tournament.category}
            </div>
            <div key={tournament.type} className={styles.result}>
              {tournament.type}
            </div>
            <div key={tournament.name} className={styles.result}>
              {tournament.name}
            </div>
            <div key={tournament.country} className={styles.result}>
              {tournament.country}
            </div>
            <div key={tournament.region} className={styles.result}>
              {tournament.region}
            </div>
            <div key={tournament.address} className={styles.result}>
              {tournament.address}
            </div>
            <div key={tournament.date} className={styles.result}>
              {tournament.date}
            </div>
          </div>
        )}
      </header>
      <div className={styles.content}>
        <div className={styles.searchContainer}>
          <TextField
            className={styles.searchInput}
            placeholder="Search..."
            inputRef={searchInputRef}
            value={searchValue}
            onChange={handleChange}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
            onKeyDown={handleKeyDown}
          />
          <Button
            className={styles.searchButton}
            variant="contained"
            onClick={handleSearch}
          >
            Search
          </Button>
        </div>
        {searchResults.length > 0 && (
          <div className={styles.resultsContainer}>
            <h2>Search Results</h2>
            {searchResults.map((pokemon) => (
              <div>
                <div key={pokemon.name} className={styles.result}>
                  {/* <a href={"detail/tournament_id/"+pastSearchValue+"/pokemon_name/"+pokemon.name}>
                    {pokemon.name}
                  </a> */}
                  <button onClick={() => {
                      router.push(`/detail/${tournament._id}/${encodeURIComponent(pokemon.name)}`);
                  }}>
                    {pokemon.name}
                  </button>
                </div>
                <div key={pokemon.usage} className={styles.result}>
                  {pokemon.usage + "%"}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
