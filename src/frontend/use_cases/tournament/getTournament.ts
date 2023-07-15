import { AxiosResponse } from "axios";
import TournamentDTO from "context/dto/TournamentDTO";
import Api from "services/Api";

export async function getTournament(
  _id: string
): Promise<AxiosResponse<TournamentDTO>> {
  const api: Api<TournamentDTO> = new Api<TournamentDTO>("https://aoemn97m79.execute-api.us-west-2.amazonaws.com/default/lambda-mongodb-scraping-data-dev-get_tournament_data");
  return api.get(``, {params: {"tournament_id": _id}});
}
