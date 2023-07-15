import React, { ReactElement, useRef, useState } from "react";
import { TextField, InputAdornment, Button } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import styles from "./Search.module.css";

const mockData = [
  {
    name: "Pikachu",
    teraTypePercentage: 12.5,
    moves: [
      { name: "Thunderbolt", percentage: 25 },
      { name: "Agility", percentage: 20 },
      { name: "Thunder Wave", percentage: 15 },
      // Add more moves as needed
    ],
    abilities: [
      { name: "Static", percentage: 70 },
      { name: "Lightning Rod", percentage: 30 },
      // Add more abilities as needed
    ],
    baseStats: {
      hp: 35,
      atk: 55,
      def: 40,
      spa: 50,
      spd: 50,
      spe: 90,
    },
  },
  // Add more mock data items as needed
];

export const Search: React.FC = (): ReactElement => {
  const searchInputRef = useRef<HTMLInputElement>(null);
  const [searchValue, setSearchValue] = useState("");
  const [searchResults, setSearchResults] = useState<any[]>([]);

  const handleSearch = () => {
    // Simulating async search request
    setTimeout(() => {
      setSearchResults(
        mockData.filter((data) => data.name.includes(searchValue))
      );
    }, 1000);
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      event.preventDefault();
      searchInputRef.current?.blur();
      handleSearch();
    }
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchValue(event.target.value);
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1 className={styles.logo}>Your Logo</h1>
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
            {searchResults.map((result, index) => (
              <div key={index} className={styles.resultItem}>
                <h3>{result.name}</h3>
                <p>Tera Type: {result.teraTypePercentage}%</p>
                <div>
                  <h4>Moves:</h4>
                  <ul>
                    {result.moves.map((move, moveIndex) => (
                      <li key={moveIndex}>
                        {move.name}: {move.percentage}%
                      </li>
                    ))}
                  </ul>
                </div>
                <div>
                  <h4>Abilities:</h4>
                  <ul>
                    {result.abilities.map((ability, abilityIndex) => (
                      <li key={abilityIndex}>
                        {ability.name}: {ability.percentage}%
                      </li>
                    ))}
                  </ul>
                </div>
                <div className={styles.statsGraph}>
                  {/* Render the graph of stats here */}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
