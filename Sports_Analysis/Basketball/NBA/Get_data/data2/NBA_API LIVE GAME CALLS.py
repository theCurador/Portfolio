from nba_api.stats.endpoints import teamdashboardbyteamperformance
from nba_api.stats.endpoints import teamdashboardbyyearoveryear
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playbyplay
from nba_api.stats.endpoints import TeamDashboardByOpponent
from nba_api.stats.static import players
from nba_api.stats.static import teams
# Get all players.
players.get_players()

# Get all teams.
teams.get_teams()

print(teams)