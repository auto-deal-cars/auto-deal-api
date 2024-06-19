""" This module contains the controller for the create vehicle """
import json
from pydantic import ValidationError

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.infrastructure.database.setup import get_db

def mark_vehicle_as_sold(event, context):
    """ Mark a Vehicle as sold """
    print(json.dumps(event))
    try:
        vehicle_id = event.get('pathParameters', {}).get('id')
        user_id = (
            event
            .get('requestContext', {})
            .get('authorizer', {})
            .get('jwt', {})
            .get('claims', {})
            .get('sub')
        )

        if not vehicle_id or not user_id:
            raise KeyError('Vehicle ID and User ID are required')

        db = next(get_db())
        repository = VehicleRepositoryAdapter(db)
        service = VehicleService(repository)
        service.mark_vehicle_as_sold(vehicle_id, user_id)

        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Vehicle marked as sold successfully!',
            })
        }
    except ValidationError as error:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Validation error',
                'errors': error.errors(
                    include_url=False
                )
            })
        }
    except KeyError as error:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Key error',
                'error': str(error)
            })
        }
    except ValueError:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'message': 'Vehicle not found'
            })
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while marking the vehicle as sold',
            })
        }
