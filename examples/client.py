import asyncio

from viam.robot.client import RobotClient
from viam.logging import getLogger
from viam.services.generic import Generic

LOGGER = getLogger(__name__)

async def connect():
    opts = RobotClient.Options.with_api_key(
      api_key='<API-Key>',
      api_key_id='<API-Key-ID>'
    )
    return await RobotClient.at_address('<robot-address>', opts)

async def main():
    machine = await connect()

    LOGGER.info('Resources:')
    LOGGER.info(machine.resource_names)

    stt = Generic.from_robot(machine, name="stt")

    LOGGER.info("Listening for speech...")
    result = await stt.do_command({"listen": []})
    LOGGER.info(f"I think I heard:\n {result["listen"]}")

    # Don't forget to close the machine when you're done!
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
