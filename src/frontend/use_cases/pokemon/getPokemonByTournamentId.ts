import { AxiosResponse } from "axios";
import PokemonDTO from "context/dto/PokemonDTO";
import Api from "services/Api";

export async function getPokemonByTournamentId(
  tournament_id: string
): Promise<AxiosResponse<PokemonDTO>> {
  const api: Api<PokemonDTO> = new Api<PokemonDTO>("https://aoemn97m79.execute-api.us-west-2.amazonaws.com/default/lambda-mongodb-scraping-data-dev-get_pokemon_data");
  return api.get(``, {params: {"tournament_id": tournament_id}});
}
