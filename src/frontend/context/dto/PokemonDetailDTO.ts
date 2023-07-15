type UsageDTO = {
    name: string;
    usage: number;
}

type DetailDTO = {
    tera_type: UsageDTO[];
    ability: UsageDTO[];
    item: UsageDTO[];
    moves: UsageDTO[];
}

type PokemonDetailDTO = {
    pokemon: DetailDTO
};

export default PokemonDetailDTO;
