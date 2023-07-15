import { AxiosResponse } from "axios";
import PokemonDetailDTO from "context/dto/PokemonDetailDTO";
import Api from "services/Api";

export async function getPokemonDetail(
  tournament_id: string, pokemon_name: string
): Promise<AxiosResponse<PokemonDetailDTO>> {
  const api: Api<PokemonDetailDTO> = new Api<PokemonDetailDTO>("https://aoemn97m79.execute-api.us-west-2.amazonaws.com/default/lambda-mongodb-scraping-data-dev-get_pokemon_detail");
  return api.get(``, {params: {"tournament_id": tournament_id, "pokemon_name": pokemon_name}});
}
