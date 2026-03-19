LÖVE 11.5 Reference

BezierCurve:evaluate

Evaluate Bézier curve at parameter t. The parameter must be between 0 and 1 (inclusive).

This function can be used to move objects along paths or tween parameters. However it should not be used to render the curve, see BezierCurve:render for that purpose.

BezierCurve:evaluate(t)

| name | type | description |
| --- | --- | --- |
| t | number | Where to evaluate the curve. |

| name | type | description |
| --- | --- | --- |
| x | number | x coordinate of the curve at parameter t. |
| y | number | y coordinate of the curve at parameter t. |


BezierCurve:getControlPoint

Get coordinates of the i-th control point. Indices start with 1.

BezierCurve:getControlPoint(i)

| name | type | description |
| --- | --- | --- |
| i | number | Index of the control point. |

| name | type | description |
| --- | --- | --- |
| x | number | Position of the control point along the x axis. |
| y | number | Position of the control point along the y axis. |


BezierCurve:getControlPointCount

Get the number of control points in the Bézier curve.

BezierCurve:getControlPointCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of control points. |


BezierCurve:getDegree

Get degree of the Bézier curve. The degree is equal to number-of-control-points - 1.

BezierCurve:getDegree()

| name | type | description |
| --- | --- | --- |
| degree | number | Degree of the Bézier curve. |


BezierCurve:getDerivative

Get the derivative of the Bézier curve.

This function can be used to rotate sprites moving along a curve in the direction of the movement and compute the direction perpendicular to the curve at some parameter t.

BezierCurve:getDerivative()

| name | type | description |
| --- | --- | --- |
| derivative | BezierCurve | The derivative curve. |


BezierCurve:getSegment

Gets a BezierCurve that corresponds to the specified segment of this BezierCurve.

BezierCurve:getSegment(startpoint, endpoint)

| name | type | description |
| --- | --- | --- |
| startpoint | number | The starting point along the curve. Must be between 0 and 1. |
| endpoint | number | The end of the segment. Must be between 0 and 1. |

| name | type | description |
| --- | --- | --- |
| curve | BezierCurve | A BezierCurve that corresponds to the specified segment. |


BezierCurve:insertControlPoint

Insert control point as the new i-th control point. Existing control points from i onwards are pushed back by 1. Indices start with 1. Negative indices wrap around: -1 is the last control point, -2 the one before the last, etc.

BezierCurve:insertControlPoint(x, y, i)

| name | type | description |
| --- | --- | --- |
| x | number | Position of the control point along the x axis. |
| y | number | Position of the control point along the y axis. |
| i | number | Index of the control point. |


BezierCurve:removeControlPoint

Removes the specified control point.

BezierCurve:removeControlPoint(index)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the control point to remove. |


BezierCurve:render

Get a list of coordinates to be used with love.graphics.line.

This function samples the Bézier curve using recursive subdivision. You can control the recursion depth using the depth parameter.

If you are just interested to know the position on the curve given a parameter, use BezierCurve:evaluate.

BezierCurve:render(depth)

| name | type | description |
| --- | --- | --- |
| depth | number | Number of recursive subdivision steps. |

| name | type | description |
| --- | --- | --- |
| coordinates | table | List of x,y-coordinate pairs of points on the curve. |


BezierCurve:renderSegment

Get a list of coordinates on a specific part of the curve, to be used with love.graphics.line.

This function samples the Bézier curve using recursive subdivision. You can control the recursion depth using the depth parameter.

If you are just need to know the position on the curve given a parameter, use BezierCurve:evaluate.

BezierCurve:renderSegment(startpoint, endpoint, depth)

| name | type | description |
| --- | --- | --- |
| startpoint | number | The starting point along the curve. Must be between 0 and 1. |
| endpoint | number | The end of the segment to render. Must be between 0 and 1. |
| depth | number | Number of recursive subdivision steps. |

| name | type | description |
| --- | --- | --- |
| coordinates | table | List of x,y-coordinate pairs of points on the specified part of the curve. |


BezierCurve:rotate

Rotate the Bézier curve by an angle.

BezierCurve:rotate(angle, ox, oy)

| name | type | description |
| --- | --- | --- |
| angle | number | Rotation angle in radians. |
| ox | number | X coordinate of the rotation center. |
| oy | number | Y coordinate of the rotation center. |


BezierCurve:scale

Scale the Bézier curve by a factor.

BezierCurve:scale(s, ox, oy)

| name | type | description |
| --- | --- | --- |
| s | number | Scale factor. |
| ox | number | X coordinate of the scaling center. |
| oy | number | Y coordinate of the scaling center. |


BezierCurve:setControlPoint

Set coordinates of the i-th control point. Indices start with 1.

BezierCurve:setControlPoint(i, x, y)

| name | type | description |
| --- | --- | --- |
| i | number | Index of the control point. |
| x | number | Position of the control point along the x axis. |
| y | number | Position of the control point along the y axis. |


BezierCurve:translate

Move the Bézier curve by an offset.

BezierCurve:translate(dx, dy)

| name | type | description |
| --- | --- | --- |
| dx | number | Offset along the x axis. |
| dy | number | Offset along the y axis. |


Body:applyAngularImpulse

Applies an angular impulse to a body. This makes a single, instantaneous addition to the body momentum.

A body with with a larger mass will react less. The reaction does '''not''' depend on the timestep, and is equivalent to applying a force continuously for 1 second. Impulses are best used to give a single push to a body. For a continuous push to a body it is better to use Body:applyForce.

Body:applyAngularImpulse(impulse)

| name | type | description |
| --- | --- | --- |
| impulse | number | The impulse in kilogram-square meter per second. |


Body:applyForce

Apply force to a Body.

A force pushes a body in a direction. A body with with a larger mass will react less. The reaction also depends on how long a force is applied: since the force acts continuously over the entire timestep, a short timestep will only push the body for a short time. Thus forces are best used for many timesteps to give a continuous push to a body (like gravity). For a single push that is independent of timestep, it is better to use Body:applyLinearImpulse.

If the position to apply the force is not given, it will act on the center of mass of the body. The part of the force not directed towards the center of mass will cause the body to spin (and depends on the rotational inertia).

Note that the force components and position must be given in world coordinates.

Body:applyForce(fx, fy)

| name | type | description |
| --- | --- | --- |
| fx | number | The x component of force to apply to the center of mass. |
| fy | number | The y component of force to apply to the center of mass. |

Body:applyForce(fx, fy, x, y)

| name | type | description |
| --- | --- | --- |
| fx | number | The x component of force to apply. |
| fy | number | The y component of force to apply. |
| x | number | The x position to apply the force. |
| y | number | The y position to apply the force. |


Body:applyLinearImpulse

Applies an impulse to a body.

This makes a single, instantaneous addition to the body momentum.

An impulse pushes a body in a direction. A body with with a larger mass will react less. The reaction does '''not''' depend on the timestep, and is equivalent to applying a force continuously for 1 second. Impulses are best used to give a single push to a body. For a continuous push to a body it is better to use Body:applyForce.

If the position to apply the impulse is not given, it will act on the center of mass of the body. The part of the impulse not directed towards the center of mass will cause the body to spin (and depends on the rotational inertia).

Note that the impulse components and position must be given in world coordinates.

Body:applyLinearImpulse(ix, iy)

| name | type | description |
| --- | --- | --- |
| ix | number | The x component of the impulse applied to the center of mass. |
| iy | number | The y component of the impulse applied to the center of mass. |

Body:applyLinearImpulse(ix, iy, x, y)

| name | type | description |
| --- | --- | --- |
| ix | number | The x component of the impulse. |
| iy | number | The y component of the impulse. |
| x | number | The x position to apply the impulse. |
| y | number | The y position to apply the impulse. |


Body:applyTorque

Apply torque to a body.

Torque is like a force that will change the angular velocity (spin) of a body. The effect will depend on the rotational inertia a body has.

Body:applyTorque(torque)

| name | type | description |
| --- | --- | --- |
| torque | number | The torque to apply. |


Body:destroy

Explicitly destroys the Body and all fixtures and joints attached to it.

An error will occur if you attempt to use the object after calling this function. In 0.7.2, when you don't have time to wait for garbage collection, this function may be used to free the object immediately.

Body:destroy()


Body:getAngle

Get the angle of the body.

The angle is measured in radians. If you need to transform it to degrees, use math.deg.

A value of 0 radians will mean 'looking to the right'. Although radians increase counter-clockwise, the y axis points down so it becomes ''clockwise'' from our point of view.

Body:getAngle()

| name | type | description |
| --- | --- | --- |
| angle | number | The angle in radians. |


Body:getAngularDamping

Gets the Angular damping of the Body

The angular damping is the ''rate of decrease of the angular velocity over time'': A spinning body with no damping and no external forces will continue spinning indefinitely. A spinning body with damping will gradually stop spinning.

Damping is not the same as friction - they can be modelled together. However, only damping is provided by Box2D (and LOVE).

Damping parameters should be between 0 and infinity, with 0 meaning no damping, and infinity meaning full damping. Normally you will use a damping value between 0 and 0.1.

Body:getAngularDamping()

| name | type | description |
| --- | --- | --- |
| damping | number | The value of the angular damping. |


Body:getAngularVelocity

Get the angular velocity of the Body.

The angular velocity is the ''rate of change of angle over time''.

It is changed in World:update by applying torques, off centre forces/impulses, and angular damping. It can be set directly with Body:setAngularVelocity.

If you need the ''rate of change of position over time'', use Body:getLinearVelocity.

Body:getAngularVelocity()

| name | type | description |
| --- | --- | --- |
| w | number | The angular velocity in radians/second. |


Body:getContacts

Gets a list of all Contacts attached to the Body.

Body:getContacts()

| name | type | description |
| --- | --- | --- |
| contacts | table | A list with all contacts associated with the Body. |


Body:getFixtures

Returns a table with all fixtures.

Body:getFixtures()

| name | type | description |
| --- | --- | --- |
| fixtures | table | A sequence with all fixtures. |


Body:getGravityScale

Returns the gravity scale factor.

Body:getGravityScale()

| name | type | description |
| --- | --- | --- |
| scale | number | The gravity scale factor. |


Body:getInertia

Gets the rotational inertia of the body.

The rotational inertia is how hard is it to make the body spin.

Body:getInertia()

| name | type | description |
| --- | --- | --- |
| inertia | number | The rotational inertial of the body. |


Body:getJoints

Returns a table containing the Joints attached to this Body.

Body:getJoints()

| name | type | description |
| --- | --- | --- |
| joints | table | A sequence with the Joints attached to the Body. |


Body:getLinearDamping

Gets the linear damping of the Body.

The linear damping is the ''rate of decrease of the linear velocity over time''. A moving body with no damping and no external forces will continue moving indefinitely, as is the case in space. A moving body with damping will gradually stop moving.

Damping is not the same as friction - they can be modelled together.

Body:getLinearDamping()

| name | type | description |
| --- | --- | --- |
| damping | number | The value of the linear damping. |


Body:getLinearVelocity

Gets the linear velocity of the Body from its center of mass.

The linear velocity is the ''rate of change of position over time''.

If you need the ''rate of change of angle over time'', use Body:getAngularVelocity.

If you need to get the linear velocity of a point different from the center of mass:

*  Body:getLinearVelocityFromLocalPoint allows you to specify the point in local coordinates.

*  Body:getLinearVelocityFromWorldPoint allows you to specify the point in world coordinates.

See page 136 of 'Essential Mathematics for Games and Interactive Applications' for definitions of local and world coordinates.

Body:getLinearVelocity()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the velocity vector |
| y | number | The y-component of the velocity vector |


Body:getLinearVelocityFromLocalPoint

Get the linear velocity of a point on the body.

The linear velocity for a point on the body is the velocity of the body center of mass plus the velocity at that point from the body spinning.

The point on the body must given in local coordinates. Use Body:getLinearVelocityFromWorldPoint to specify this with world coordinates.

Body:getLinearVelocityFromLocalPoint(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x position to measure velocity. |
| y | number | The y position to measure velocity. |

| name | type | description |
| --- | --- | --- |
| vx | number | The x component of velocity at point (x,y). |
| vy | number | The y component of velocity at point (x,y). |


Body:getLinearVelocityFromWorldPoint

Get the linear velocity of a point on the body.

The linear velocity for a point on the body is the velocity of the body center of mass plus the velocity at that point from the body spinning.

The point on the body must given in world coordinates. Use Body:getLinearVelocityFromLocalPoint to specify this with local coordinates.

Body:getLinearVelocityFromWorldPoint(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x position to measure velocity. |
| y | number | The y position to measure velocity. |

| name | type | description |
| --- | --- | --- |
| vx | number | The x component of velocity at point (x,y). |
| vy | number | The y component of velocity at point (x,y). |


Body:getLocalCenter

Get the center of mass position in local coordinates.

Use Body:getWorldCenter to get the center of mass in world coordinates.

Body:getLocalCenter()

| name | type | description |
| --- | --- | --- |
| x | number | The x coordinate of the center of mass. |
| y | number | The y coordinate of the center of mass. |


Body:getLocalPoint

Transform a point from world coordinates to local coordinates.

Body:getLocalPoint(worldX, worldY)

| name | type | description |
| --- | --- | --- |
| worldX | number | The x position in world coordinates. |
| worldY | number | The y position in world coordinates. |

| name | type | description |
| --- | --- | --- |
| localX | number | The x position in local coordinates. |
| localY | number | The y position in local coordinates. |


Body:getLocalPoints

Transforms multiple points from world coordinates to local coordinates.

Body:getLocalPoints(x1, y1, x2, y2, ...)

| name | type | description |
| --- | --- | --- |
| x1 | number | (Argument) The x position of the first point. |
| y1 | number | (Argument) The y position of the first point. |
| x2 | number | (Argument) The x position of the second point. |
| y2 | number | (Argument) The y position of the second point. |
| ... | number | (Argument) You can continue passing x and y position of the points. |

| name | type | description |
| --- | --- | --- |
| x1 | number | (Result) The transformed x position of the first point. |
| y1 | number | (Result) The transformed y position of the first point. |
| x2 | number | (Result) The transformed x position of the second point. |
| y2 | number | (Result) The transformed y position of the second point. |
| ... | number | (Result) Additional transformed x and y position of the points. |


Body:getLocalVector

Transform a vector from world coordinates to local coordinates.

Body:getLocalVector(worldX, worldY)

| name | type | description |
| --- | --- | --- |
| worldX | number | The vector x component in world coordinates. |
| worldY | number | The vector y component in world coordinates. |

| name | type | description |
| --- | --- | --- |
| localX | number | The vector x component in local coordinates. |
| localY | number | The vector y component in local coordinates. |


Body:getMass

Get the mass of the body.

Static bodies always have a mass of 0.

Body:getMass()

| name | type | description |
| --- | --- | --- |
| mass | number | The mass of the body (in kilograms). |


Body:getMassData

Returns the mass, its center, and the rotational inertia.

Body:getMassData()

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the center of mass. |
| y | number | The y position of the center of mass. |
| mass | number | The mass of the body. |
| inertia | number | The rotational inertia. |


Body:getPosition

Get the position of the body.

Note that this may not be the center of mass of the body.

Body:getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | The x position. |
| y | number | The y position. |


Body:getTransform

Get the position and angle of the body.

Note that the position may not be the center of mass of the body. An angle of 0 radians will mean 'looking to the right'. Although radians increase counter-clockwise, the y axis points down so it becomes clockwise from our point of view.

Body:getTransform()

| name | type | description |
| --- | --- | --- |
| x | number | The x component of the position. |
| y | number | The y component of the position. |
| angle | number | The angle in radians. |


Body:getType

Returns the type of the body.

Body:getType()

| name | type | description |
| --- | --- | --- |
| type | BodyType | The body type. |


Body:getUserData

Returns the Lua value associated with this Body.

Body:getUserData()

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value associated with the Body. |


Body:getWorld

Gets the World the body lives in.

Body:getWorld()

| name | type | description |
| --- | --- | --- |
| world | World | The world the body lives in. |


Body:getWorldCenter

Get the center of mass position in world coordinates.

Use Body:getLocalCenter to get the center of mass in local coordinates.

Body:getWorldCenter()

| name | type | description |
| --- | --- | --- |
| x | number | The x coordinate of the center of mass. |
| y | number | The y coordinate of the center of mass. |


Body:getWorldPoint

Transform a point from local coordinates to world coordinates.

Body:getWorldPoint(localX, localY)

| name | type | description |
| --- | --- | --- |
| localX | number | The x position in local coordinates. |
| localY | number | The y position in local coordinates. |

| name | type | description |
| --- | --- | --- |
| worldX | number | The x position in world coordinates. |
| worldY | number | The y position in world coordinates. |


Body:getWorldPoints

Transforms multiple points from local coordinates to world coordinates.

Body:getWorldPoints(x1, y1, x2, y2)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the first point. |
| y1 | number | The y position of the first point. |
| x2 | number | The x position of the second point. |
| y2 | number | The y position of the second point. |

| name | type | description |
| --- | --- | --- |
| x1 | number | The transformed x position of the first point. |
| y1 | number | The transformed y position of the first point. |
| x2 | number | The transformed x position of the second point. |
| y2 | number | The transformed y position of the second point. |


Body:getWorldVector

Transform a vector from local coordinates to world coordinates.

Body:getWorldVector(localX, localY)

| name | type | description |
| --- | --- | --- |
| localX | number | The vector x component in local coordinates. |
| localY | number | The vector y component in local coordinates. |

| name | type | description |
| --- | --- | --- |
| worldX | number | The vector x component in world coordinates. |
| worldY | number | The vector y component in world coordinates. |


Body:getX

Get the x position of the body in world coordinates.

Body:getX()

| name | type | description |
| --- | --- | --- |
| x | number | The x position in world coordinates. |


Body:getY

Get the y position of the body in world coordinates.

Body:getY()

| name | type | description |
| --- | --- | --- |
| y | number | The y position in world coordinates. |


Body:isActive

Returns whether the body is actively used in the simulation.

Body:isActive()

| name | type | description |
| --- | --- | --- |
| status | boolean | True if the body is active or false if not. |


Body:isAwake

Returns the sleep status of the body.

Body:isAwake()

| name | type | description |
| --- | --- | --- |
| status | boolean | True if the body is awake or false if not. |


Body:isBullet

Get the bullet status of a body.

There are two methods to check for body collisions:

*  at their location when the world is updated (default)

*  using continuous collision detection (CCD)

The default method is efficient, but a body moving very quickly may sometimes jump over another body without producing a collision. A body that is set as a bullet will use CCD. This is less efficient, but is guaranteed not to jump when moving quickly.

Note that static bodies (with zero mass) always use CCD, so your walls will not let a fast moving body pass through even if it is not a bullet.

Body:isBullet()

| name | type | description |
| --- | --- | --- |
| status | boolean | The bullet status of the body. |


Body:isDestroyed

Gets whether the Body is destroyed. Destroyed bodies cannot be used.

Body:isDestroyed()

| name | type | description |
| --- | --- | --- |
| destroyed | boolean | Whether the Body is destroyed. |


Body:isFixedRotation

Returns whether the body rotation is locked.

Body:isFixedRotation()

| name | type | description |
| --- | --- | --- |
| fixed | boolean | True if the body's rotation is locked or false if not. |


Body:isSleepingAllowed

Returns the sleeping behaviour of the body.

Body:isSleepingAllowed()

| name | type | description |
| --- | --- | --- |
| allowed | boolean | True if the body is allowed to sleep or false if not. |


Body:isTouching

Gets whether the Body is touching the given other Body.

Body:isTouching(otherbody)

| name | type | description |
| --- | --- | --- |
| otherbody | Body | The other body to check. |

| name | type | description |
| --- | --- | --- |
| touching | boolean | True if this body is touching the other body, false otherwise. |


Body:resetMassData

Resets the mass of the body by recalculating it from the mass properties of the fixtures.

Body:resetMassData()


Body:setActive

Sets whether the body is active in the world.

An inactive body does not take part in the simulation. It will not move or cause any collisions.

Body:setActive(active)

| name | type | description |
| --- | --- | --- |
| active | boolean | If the body is active or not. |


Body:setAngle

Set the angle of the body.

The angle is measured in radians. If you need to transform it from degrees, use math.rad.

A value of 0 radians will mean 'looking to the right'. Although radians increase counter-clockwise, the y axis points down so it becomes ''clockwise'' from our point of view.

It is possible to cause a collision with another body by changing its angle.

Body:setAngle(angle)

| name | type | description |
| --- | --- | --- |
| angle | number | The angle in radians. |


Body:setAngularDamping

Sets the angular damping of a Body

See Body:getAngularDamping for a definition of angular damping.

Angular damping can take any value from 0 to infinity. It is recommended to stay between 0 and 0.1, though. Other values will look unrealistic.

Body:setAngularDamping(damping)

| name | type | description |
| --- | --- | --- |
| damping | number | The new angular damping. |


Body:setAngularVelocity

Sets the angular velocity of a Body.

The angular velocity is the ''rate of change of angle over time''.

This function will not accumulate anything; any impulses previously applied since the last call to World:update will be lost.

Body:setAngularVelocity(w)

| name | type | description |
| --- | --- | --- |
| w | number | The new angular velocity, in radians per second |


Body:setAwake

Wakes the body up or puts it to sleep.

Body:setAwake(awake)

| name | type | description |
| --- | --- | --- |
| awake | boolean | The body sleep status. |


Body:setBullet

Set the bullet status of a body.

There are two methods to check for body collisions:

*  at their location when the world is updated (default)

*  using continuous collision detection (CCD)

The default method is efficient, but a body moving very quickly may sometimes jump over another body without producing a collision. A body that is set as a bullet will use CCD. This is less efficient, but is guaranteed not to jump when moving quickly.

Note that static bodies (with zero mass) always use CCD, so your walls will not let a fast moving body pass through even if it is not a bullet.

Body:setBullet(status)

| name | type | description |
| --- | --- | --- |
| status | boolean | The bullet status of the body. |


Body:setFixedRotation

Set whether a body has fixed rotation.

Bodies with fixed rotation don't vary the speed at which they rotate. Calling this function causes the mass to be reset.

Body:setFixedRotation(isFixed)

| name | type | description |
| --- | --- | --- |
| isFixed | boolean | Whether the body should have fixed rotation. |


Body:setGravityScale

Sets a new gravity scale factor for the body.

Body:setGravityScale(scale)

| name | type | description |
| --- | --- | --- |
| scale | number | The new gravity scale factor. |


Body:setInertia

Set the inertia of a body.

Body:setInertia(inertia)

| name | type | description |
| --- | --- | --- |
| inertia | number | The new moment of inertia, in kilograms * pixel squared. |


Body:setLinearDamping

Sets the linear damping of a Body

See Body:getLinearDamping for a definition of linear damping.

Linear damping can take any value from 0 to infinity. It is recommended to stay between 0 and 0.1, though. Other values will make the objects look 'floaty'(if gravity is enabled).

Body:setLinearDamping(ld)

| name | type | description |
| --- | --- | --- |
| ld | number | The new linear damping |


Body:setLinearVelocity

Sets a new linear velocity for the Body.

This function will not accumulate anything; any impulses previously applied since the last call to World:update will be lost.

Body:setLinearVelocity(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the velocity vector. |
| y | number | The y-component of the velocity vector. |


Body:setMass

Sets a new body mass.

Body:setMass(mass)

| name | type | description |
| --- | --- | --- |
| mass | number | The mass, in kilograms. |


Body:setMassData

Overrides the calculated mass data.

Body:setMassData(x, y, mass, inertia)

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the center of mass. |
| y | number | The y position of the center of mass. |
| mass | number | The mass of the body. |
| inertia | number | The rotational inertia. |


Body:setPosition

Set the position of the body.

Note that this may not be the center of mass of the body.

This function cannot wake up the body.

Body:setPosition(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x position. |
| y | number | The y position. |


Body:setSleepingAllowed

Sets the sleeping behaviour of the body. Should sleeping be allowed, a body at rest will automatically sleep. A sleeping body is not simulated unless it collided with an awake body. Be wary that one can end up with a situation like a floating sleeping body if the floor was removed.

Body:setSleepingAllowed(allowed)

| name | type | description |
| --- | --- | --- |
| allowed | boolean | True if the body is allowed to sleep or false if not. |


Body:setTransform

Set the position and angle of the body.

Note that the position may not be the center of mass of the body. An angle of 0 radians will mean 'looking to the right'. Although radians increase counter-clockwise, the y axis points down so it becomes clockwise from our point of view.

This function cannot wake up the body.

Body:setTransform(x, y, angle)

| name | type | description |
| --- | --- | --- |
| x | number | The x component of the position. |
| y | number | The y component of the position. |
| angle | number | The angle in radians. |


Body:setType

Sets a new body type.

Body:setType(type)

| name | type | description |
| --- | --- | --- |
| type | BodyType | The new type. |


Body:setUserData

Associates a Lua value with the Body.

To delete the reference, explicitly pass nil.

Body:setUserData(value)

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value to associate with the Body. |


Body:setX

Set the x position of the body.

This function cannot wake up the body.

Body:setX(x)

| name | type | description |
| --- | --- | --- |
| x | number | The x position. |


Body:setY

Set the y position of the body.

This function cannot wake up the body.

Body:setY(y)

| name | type | description |
| --- | --- | --- |
| y | number | The y position. |


Canvas:generateMipmaps

Generates mipmaps for the Canvas, based on the contents of the highest-resolution mipmap level.

The Canvas must be created with mipmaps set to a MipmapMode other than 'none' for this function to work. It should only be called while the Canvas is not the active render target.

If the mipmap mode is set to 'auto', this function is automatically called inside love.graphics.setCanvas when switching from this Canvas to another Canvas or to the main screen.

Canvas:generateMipmaps()


Canvas:getMSAA

Gets the number of multisample antialiasing (MSAA) samples used when drawing to the Canvas.

This may be different than the number used as an argument to love.graphics.newCanvas if the system running LÖVE doesn't support that number.

Canvas:getMSAA()

| name | type | description |
| --- | --- | --- |
| samples | number | The number of multisample antialiasing samples used by the canvas when drawing to it. |


Canvas:getMipmapMode

Gets the MipmapMode this Canvas was created with.

Canvas:getMipmapMode()

| name | type | description |
| --- | --- | --- |
| mode | MipmapMode | The mipmap mode this Canvas was created with. |


Canvas:newImageData

Generates ImageData from the contents of the Canvas.

Canvas:newImageData()

| name | type | description |
| --- | --- | --- |
| data | ImageData | The new ImageData made from the Canvas' contents. |

Canvas:newImageData(slice, mipmap, x, y, width, height)

| name | type | description |
| --- | --- | --- |
| slice | number | The cubemap face index, array index, or depth layer for cubemap, array, or volume type Canvases, respectively. This argument is ignored for regular 2D canvases. |
| mipmap | number | The mipmap index to use, for Canvases with mipmaps. |
| x | number | The x-axis of the top-left corner (in pixels) of the area within the Canvas to capture. |
| y | number | The y-axis of the top-left corner (in pixels) of the area within the Canvas to capture. |
| width | number | The width in pixels of the area within the Canvas to capture. |
| height | number | The height in pixels of the area within the Canvas to capture. |

| name | type | description |
| --- | --- | --- |
| data | ImageData | The new ImageData made from the Canvas' contents. |


Canvas:renderTo

Render to the Canvas using a function.

This is a shortcut to love.graphics.setCanvas:

canvas:renderTo( func )

is the same as

love.graphics.setCanvas( canvas )

func()

love.graphics.setCanvas()

Canvas:renderTo(func, ...)

| name | type | description |
| --- | --- | --- |
| func | function | A function performing drawing operations. |
| ... | any | Additional arguments to call the function with. |


ChainShape:getChildEdge

Returns a child of the shape as an EdgeShape.

ChainShape:getChildEdge(index)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the child. |

| name | type | description |
| --- | --- | --- |
| shape | EdgeShape | The child as an EdgeShape. |


ChainShape:getNextVertex

Gets the vertex that establishes a connection to the next shape.

Setting next and previous ChainShape vertices can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

ChainShape:getNextVertex()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex, or nil if ChainShape:setNextVertex hasn't been called. |
| y | number | The y-component of the vertex, or nil if ChainShape:setNextVertex hasn't been called. |


ChainShape:getPoint

Returns a point of the shape.

ChainShape:getPoint(index)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the point to return. |

| name | type | description |
| --- | --- | --- |
| x | number | The x-coordinate of the point. |
| y | number | The y-coordinate of the point. |


ChainShape:getPoints

Returns all points of the shape.

ChainShape:getPoints()

| name | type | description |
| --- | --- | --- |
| x1 | number | The x-coordinate of the first point. |
| y1 | number | The y-coordinate of the first point. |
| x2 | number | The x-coordinate of the second point. |
| y2 | number | The y-coordinate of the second point. |


ChainShape:getPreviousVertex

Gets the vertex that establishes a connection to the previous shape.

Setting next and previous ChainShape vertices can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

ChainShape:getPreviousVertex()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex, or nil if ChainShape:setPreviousVertex hasn't been called. |
| y | number | The y-component of the vertex, or nil if ChainShape:setPreviousVertex hasn't been called. |


ChainShape:getVertexCount

Returns the number of vertices the shape has.

ChainShape:getVertexCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of vertices. |


ChainShape:setNextVertex

Sets a vertex that establishes a connection to the next shape.

This can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

ChainShape:setNextVertex(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex. |
| y | number | The y-component of the vertex. |


ChainShape:setPreviousVertex

Sets a vertex that establishes a connection to the previous shape.

This can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

ChainShape:setPreviousVertex(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex. |
| y | number | The y-component of the vertex. |


Channel:clear

Clears all the messages in the Channel queue.

Channel:clear()


Channel:demand

Retrieves the value of a Channel message and removes it from the message queue.

It waits until a message is in the queue then returns the message value.

Channel:demand()

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |

Channel:demand(timeout)

| name | type | description |
| --- | --- | --- |
| timeout | number | The maximum amount of time to wait. |

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message or nil if the timeout expired. |


Channel:getCount

Retrieves the number of messages in the thread Channel queue.

Channel:getCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of messages in the queue. |


Channel:hasRead

Gets whether a pushed value has been popped or otherwise removed from the Channel.

Channel:hasRead(id)

| name | type | description |
| --- | --- | --- |
| id | number | An id value previously returned by Channel:push. |

| name | type | description |
| --- | --- | --- |
| hasread | boolean | Whether the value represented by the id has been removed from the Channel via Channel:pop, Channel:demand, or Channel:clear. |


Channel:peek

Retrieves the value of a Channel message, but leaves it in the queue.

It returns nil if there's no message in the queue.

Channel:peek()

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |


Channel:performAtomic

Executes the specified function atomically with respect to this Channel.

Calling multiple methods in a row on the same Channel is often useful. However if multiple Threads are calling this Channel's methods at the same time, the different calls on each Thread might end up interleaved (e.g. one or more of the second thread's calls may happen in between the first thread's calls.)

This method avoids that issue by making sure the Thread calling the method has exclusive access to the Channel until the specified function has returned.

Channel:performAtomic(func, ...)

| name | type | description |
| --- | --- | --- |
| func | function | The function to call, the form of function(channel, arg1, arg2, ...) end. The Channel is passed as the first argument to the function when it is called. |
| ... | any | Additional arguments that the given function will receive when it is called. |

| name | type | description |
| --- | --- | --- |
| ret1 | any | The first return value of the given function (if any.) |
| ... | any | Any other return values. |


Channel:pop

Retrieves the value of a Channel message and removes it from the message queue.

It returns nil if there are no messages in the queue.

Channel:pop()

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |


Channel:push

Send a message to the thread Channel.

See Variant for the list of supported types.

Channel:push(value)

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |

| name | type | description |
| --- | --- | --- |
| id | number | Identifier which can be supplied to Channel:hasRead |


Channel:supply

Send a message to the thread Channel and wait for a thread to accept it.

See Variant for the list of supported types.

Channel:supply(value)

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the message was successfully supplied (always true). |

Channel:supply(value, timeout)

| name | type | description |
| --- | --- | --- |
| value | Variant | The contents of the message. |
| timeout | number | The maximum amount of time to wait. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the message was successfully supplied before the timeout expired. |


CircleShape:getPoint

Gets the center point of the circle shape.

CircleShape:getPoint()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the center point of the circle. |
| y | number | The y-component of the center point of the circle. |


CircleShape:getRadius

Gets the radius of the circle shape.

CircleShape:getRadius()

| name | type | description |
| --- | --- | --- |
| radius | number | The radius of the circle |


CircleShape:setPoint

Sets the location of the center of the circle shape.

CircleShape:setPoint(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the new center point of the circle. |
| y | number | The y-component of the new center point of the circle. |


CircleShape:setRadius

Sets the radius of the circle.

CircleShape:setRadius(radius)

| name | type | description |
| --- | --- | --- |
| radius | number | The radius of the circle |


CompressedData:getFormat

Gets the compression format of the CompressedData.

CompressedData:getFormat()

| name | type | description |
| --- | --- | --- |
| format | CompressedDataFormat | The format of the CompressedData. |


CompressedImageData:getDimensions

Gets the width and height of the CompressedImageData.

CompressedImageData:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the CompressedImageData. |
| height | number | The height of the CompressedImageData. |

CompressedImageData:getDimensions(level)

| name | type | description |
| --- | --- | --- |
| level | number | A mipmap level. Must be in the range of CompressedImageData:getMipmapCount(). |

| name | type | description |
| --- | --- | --- |
| width | number | The width of a specific mipmap level of the CompressedImageData. |
| height | number | The height of a specific mipmap level of the CompressedImageData. |


CompressedImageData:getFormat

Gets the format of the CompressedImageData.

CompressedImageData:getFormat()

| name | type | description |
| --- | --- | --- |
| format | CompressedImageFormat | The format of the CompressedImageData. |


CompressedImageData:getHeight

Gets the height of the CompressedImageData.

CompressedImageData:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the CompressedImageData. |

CompressedImageData:getHeight(level)

| name | type | description |
| --- | --- | --- |
| level | number | A mipmap level. Must be in the range of CompressedImageData:getMipmapCount(). |

| name | type | description |
| --- | --- | --- |
| height | number | The height of a specific mipmap level of the CompressedImageData. |


CompressedImageData:getMipmapCount

Gets the number of mipmap levels in the CompressedImageData. The base mipmap level (original image) is included in the count.

CompressedImageData:getMipmapCount()

| name | type | description |
| --- | --- | --- |
| mipmaps | number | The number of mipmap levels stored in the CompressedImageData. |


CompressedImageData:getWidth

Gets the width of the CompressedImageData.

CompressedImageData:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the CompressedImageData. |

CompressedImageData:getWidth(level)

| name | type | description |
| --- | --- | --- |
| level | number | A mipmap level. Must be in the range of  CompressedImageData:getMipmapCount(). |

| name | type | description |
| --- | --- | --- |
| width | number | The width of a specific mipmap level of the CompressedImageData. |


Contact:getChildren

Gets the child indices of the shapes of the two colliding fixtures. For ChainShapes, an index of 1 is the first edge in the chain.
Used together with Fixture:rayCast or ChainShape:getChildEdge.

Contact:getChildren()

| name | type | description |
| --- | --- | --- |
| indexA | number | The child index of the first fixture's shape. |
| indexB | number | The child index of the second fixture's shape. |


Contact:getFixtures

Gets the two Fixtures that hold the shapes that are in contact.

Contact:getFixtures()

| name | type | description |
| --- | --- | --- |
| fixtureA | Fixture | The first Fixture. |
| fixtureB | Fixture | The second Fixture. |


Contact:getFriction

Get the friction between two shapes that are in contact.

Contact:getFriction()

| name | type | description |
| --- | --- | --- |
| friction | number | The friction of the contact. |


Contact:getNormal

Get the normal vector between two shapes that are in contact.

This function returns the coordinates of a unit vector that points from the first shape to the second.

Contact:getNormal()

| name | type | description |
| --- | --- | --- |
| nx | number | The x component of the normal vector. |
| ny | number | The y component of the normal vector. |


Contact:getPositions

Returns the contact points of the two colliding fixtures. There can be one or two points.

Contact:getPositions()

| name | type | description |
| --- | --- | --- |
| x1 | number | The x coordinate of the first contact point. |
| y1 | number | The y coordinate of the first contact point. |
| x2 | number | The x coordinate of the second contact point. |
| y2 | number | The y coordinate of the second contact point. |


Contact:getRestitution

Get the restitution between two shapes that are in contact.

Contact:getRestitution()

| name | type | description |
| --- | --- | --- |
| restitution | number | The restitution between the two shapes. |


Contact:isEnabled

Returns whether the contact is enabled. The collision will be ignored if a contact gets disabled in the preSolve callback.

Contact:isEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false otherwise. |


Contact:isTouching

Returns whether the two colliding fixtures are touching each other.

Contact:isTouching()

| name | type | description |
| --- | --- | --- |
| touching | boolean | True if they touch or false if not. |


Contact:resetFriction

Resets the contact friction to the mixture value of both fixtures.

Contact:resetFriction()


Contact:resetRestitution

Resets the contact restitution to the mixture value of both fixtures.

Contact:resetRestitution()


Contact:setEnabled

Enables or disables the contact.

Contact:setEnabled(enabled)

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True to enable or false to disable. |


Contact:setFriction

Sets the contact friction.

Contact:setFriction(friction)

| name | type | description |
| --- | --- | --- |
| friction | number | The contact friction. |


Contact:setRestitution

Sets the contact restitution.

Contact:setRestitution(restitution)

| name | type | description |
| --- | --- | --- |
| restitution | number | The contact restitution. |


Cursor:getType

Gets the type of the Cursor.

Cursor:getType()

| name | type | description |
| --- | --- | --- |
| ctype | CursorType | The type of the Cursor. |


Data:clone

Creates a new copy of the Data object.

Data:clone()

| name | type | description |
| --- | --- | --- |
| clone | Data | The new copy. |


Data:getFFIPointer

Gets an FFI pointer to the Data.

This function should be preferred instead of Data:getPointer because the latter uses light userdata which can't store more all possible memory addresses on some new ARM64 architectures, when LuaJIT is used.

Data:getFFIPointer()

| name | type | description |
| --- | --- | --- |
| pointer | cdata | A raw void* pointer to the Data, or nil if FFI is unavailable. |


Data:getPointer

Gets a pointer to the Data. Can be used with libraries such as LuaJIT's FFI.

Data:getPointer()

| name | type | description |
| --- | --- | --- |
| pointer | light userdata | A raw pointer to the Data. |


Data:getSize

Gets the Data's size in bytes.

Data:getSize()

| name | type | description |
| --- | --- | --- |
| size | number | The size of the Data in bytes. |


Data:getString

Gets the full Data as a string.

Data:getString()

| name | type | description |
| --- | --- | --- |
| data | string | The raw data. |


Decoder:clone

Creates a new copy of current decoder.

The new decoder will start decoding from the beginning of the audio stream.

Decoder:clone()

| name | type | description |
| --- | --- | --- |
| decoder | Decoder | New copy of the decoder. |


Decoder:decode

Decodes the audio and returns a SoundData object containing the decoded audio data.

Decoder:decode()

| name | type | description |
| --- | --- | --- |
| soundData | SoundData | Decoded audio data. |


Decoder:getBitDepth

Returns the number of bits per sample.

Decoder:getBitDepth()

| name | type | description |
| --- | --- | --- |
| bitDepth | number | Either 8, or 16. |


Decoder:getChannelCount

Returns the number of channels in the stream.

Decoder:getChannelCount()

| name | type | description |
| --- | --- | --- |
| channels | number | 1 for mono, 2 for stereo. |


Decoder:getDuration

Gets the duration of the sound file. It may not always be sample-accurate, and it may return -1 if the duration cannot be determined at all.

Decoder:getDuration()

| name | type | description |
| --- | --- | --- |
| duration | number | The duration of the sound file in seconds, or -1 if it cannot be determined. |


Decoder:getSampleRate

Returns the sample rate of the Decoder.

Decoder:getSampleRate()

| name | type | description |
| --- | --- | --- |
| rate | number | Number of samples per second. |


Decoder:seek

Sets the currently playing position of the Decoder.

Decoder:seek(offset)

| name | type | description |
| --- | --- | --- |
| offset | number | The position to seek to, in seconds. |


DistanceJoint:getDampingRatio

Gets the damping ratio.

DistanceJoint:getDampingRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The damping ratio. |


DistanceJoint:getFrequency

Gets the response speed.

DistanceJoint:getFrequency()

| name | type | description |
| --- | --- | --- |
| Hz | number | The response speed. |


DistanceJoint:getLength

Gets the equilibrium distance between the two Bodies.

DistanceJoint:getLength()

| name | type | description |
| --- | --- | --- |
| l | number | The length between the two Bodies. |


DistanceJoint:setDampingRatio

Sets the damping ratio.

DistanceJoint:setDampingRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The damping ratio. |


DistanceJoint:setFrequency

Sets the response speed.

DistanceJoint:setFrequency(Hz)

| name | type | description |
| --- | --- | --- |
| Hz | number | The response speed. |


DistanceJoint:setLength

Sets the equilibrium distance between the two Bodies.

DistanceJoint:setLength(l)

| name | type | description |
| --- | --- | --- |
| l | number | The length between the two Bodies. |


EdgeShape:getNextVertex

Gets the vertex that establishes a connection to the next shape.

Setting next and previous EdgeShape vertices can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

EdgeShape:getNextVertex()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex, or nil if EdgeShape:setNextVertex hasn't been called. |
| y | number | The y-component of the vertex, or nil if EdgeShape:setNextVertex hasn't been called. |


EdgeShape:getPoints

Returns the local coordinates of the edge points.

EdgeShape:getPoints()

| name | type | description |
| --- | --- | --- |
| x1 | number | The x-component of the first vertex. |
| y1 | number | The y-component of the first vertex. |
| x2 | number | The x-component of the second vertex. |
| y2 | number | The y-component of the second vertex. |


EdgeShape:getPreviousVertex

Gets the vertex that establishes a connection to the previous shape.

Setting next and previous EdgeShape vertices can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

EdgeShape:getPreviousVertex()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex, or nil if EdgeShape:setPreviousVertex hasn't been called. |
| y | number | The y-component of the vertex, or nil if EdgeShape:setPreviousVertex hasn't been called. |


EdgeShape:setNextVertex

Sets a vertex that establishes a connection to the next shape.

This can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

EdgeShape:setNextVertex(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex. |
| y | number | The y-component of the vertex. |


EdgeShape:setPreviousVertex

Sets a vertex that establishes a connection to the previous shape.

This can help prevent unwanted collisions when a flat shape slides along the edge and moves over to the new shape.

EdgeShape:setPreviousVertex(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the vertex. |
| y | number | The y-component of the vertex. |


File:close

Closes a File.

File:close()

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether closing was successful. |


File:flush

Flushes any buffered written data in the file to the disk.

File:flush()

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the file successfully flushed any buffered data to the disk. |
| err | string | The error string, if an error occurred and the file could not be flushed. |


File:getBuffer

Gets the buffer mode of a file.

File:getBuffer()

| name | type | description |
| --- | --- | --- |
| mode | BufferMode | The current buffer mode of the file. |
| size | number | The maximum size in bytes of the file's buffer. |


File:getFilename

Gets the filename that the File object was created with. If the file object originated from the love.filedropped callback, the filename will be the full platform-dependent file path.

File:getFilename()

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the File. |


File:getMode

Gets the FileMode the file has been opened with.

File:getMode()

| name | type | description |
| --- | --- | --- |
| mode | FileMode | The mode this file has been opened with. |


File:getSize

Returns the file size.

File:getSize()

| name | type | description |
| --- | --- | --- |
| size | number | The file size in bytes. |


File:isEOF

Gets whether end-of-file has been reached.

File:isEOF()

| name | type | description |
| --- | --- | --- |
| eof | boolean | Whether EOF has been reached. |


File:isOpen

Gets whether the file is open.

File:isOpen()

| name | type | description |
| --- | --- | --- |
| open | boolean | True if the file is currently open, false otherwise. |


File:lines

Iterate over all the lines in a file.

File:lines()

| name | type | description |
| --- | --- | --- |
| iterator | function | The iterator (can be used in for loops). |


File:open

Open the file for write, read or append.

File:open(mode)

| name | type | description |
| --- | --- | --- |
| mode | FileMode | The mode to open the file in. |

| name | type | description |
| --- | --- | --- |
| ok | boolean | True on success, false otherwise. |
| err | string | The error string if an error occurred. |


File:read

Read a number of bytes from a file.

File:read(bytes)

| name | type | description |
| --- | --- | --- |
| bytes | number | The number of bytes to read. |

| name | type | description |
| --- | --- | --- |
| contents | string | The contents of the read bytes. |
| size | number | How many bytes have been read. |

File:read(container, bytes)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the file's contents as. |
| bytes | number | The number of bytes to read. |

| name | type | description |
| --- | --- | --- |
| contents | FileData or string | FileData or string containing the read bytes. |
| size | number | How many bytes have been read. |


File:seek

Seek to a position in a file

File:seek(pos)

| name | type | description |
| --- | --- | --- |
| pos | number | The position to seek to |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the operation was successful |


File:setBuffer

Sets the buffer mode for a file opened for writing or appending. Files with buffering enabled will not write data to the disk until the buffer size limit is reached, depending on the buffer mode.

File:flush will force any buffered data to be written to the disk.

File:setBuffer(mode, size)

| name | type | description |
| --- | --- | --- |
| mode | BufferMode | The buffer mode to use. |
| size | number | The maximum size in bytes of the file's buffer. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the buffer mode was successfully set. |
| errorstr | string | The error string, if the buffer mode could not be set and an error occurred. |


File:tell

Returns the position in the file.

File:tell()

| name | type | description |
| --- | --- | --- |
| pos | number | The current position. |


File:write

Write data to a file.

File:write(data, size)

| name | type | description |
| --- | --- | --- |
| data | string | The string data to write. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the operation was successful. |
| err | string | The error string if an error occurred. |

File:write(data, size)

| name | type | description |
| --- | --- | --- |
| data | Data | The Data object to write. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the operation was successful. |
| errorstr | string | The error string if an error occurred. |


FileData:getExtension

Gets the extension of the FileData.

FileData:getExtension()

| name | type | description |
| --- | --- | --- |
| ext | string | The extension of the file the FileData represents. |


FileData:getFilename

Gets the filename of the FileData.

FileData:getFilename()

| name | type | description |
| --- | --- | --- |
| name | string | The name of the file the FileData represents. |


Fixture:destroy

Destroys the fixture.

Fixture:destroy()


Fixture:getBody

Returns the body to which the fixture is attached.

Fixture:getBody()

| name | type | description |
| --- | --- | --- |
| body | Body | The parent body. |


Fixture:getBoundingBox

Returns the points of the fixture bounding box. In case the fixture has multiple children a 1-based index can be specified. For example, a fixture will have multiple children with a chain shape.

Fixture:getBoundingBox(index)

| name | type | description |
| --- | --- | --- |
| index | number | A bounding box of the fixture. |

| name | type | description |
| --- | --- | --- |
| topLeftX | number | The x position of the top-left point. |
| topLeftY | number | The y position of the top-left point. |
| bottomRightX | number | The x position of the bottom-right point. |
| bottomRightY | number | The y position of the bottom-right point. |


Fixture:getCategory

Returns the categories the fixture belongs to.

Fixture:getCategory()

| name | type | description |
| --- | --- | --- |
| ... | number | The categories. |


Fixture:getDensity

Returns the density of the fixture.

Fixture:getDensity()

| name | type | description |
| --- | --- | --- |
| density | number | The fixture density in kilograms per square meter. |


Fixture:getFilterData

Returns the filter data of the fixture.

Categories and masks are encoded as the bits of a 16-bit integer.

Fixture:getFilterData()

| name | type | description |
| --- | --- | --- |
| categories | number | The categories as an integer from 0 to 65535. |
| mask | number | The mask as an integer from 0 to 65535. |
| group | number | The group as an integer from -32768 to 32767. |


Fixture:getFriction

Returns the friction of the fixture.

Fixture:getFriction()

| name | type | description |
| --- | --- | --- |
| friction | number | The fixture friction. |


Fixture:getGroupIndex

Returns the group the fixture belongs to. Fixtures with the same group will always collide if the group is positive or never collide if it's negative. The group zero means no group.

The groups range from -32768 to 32767.

Fixture:getGroupIndex()

| name | type | description |
| --- | --- | --- |
| group | number | The group of the fixture. |


Fixture:getMask

Returns which categories this fixture should '''NOT''' collide with.

Fixture:getMask()

| name | type | description |
| --- | --- | --- |
| ... | number | The masks. |


Fixture:getMassData

Returns the mass, its center and the rotational inertia.

Fixture:getMassData()

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the center of mass. |
| y | number | The y position of the center of mass. |
| mass | number | The mass of the fixture. |
| inertia | number | The rotational inertia. |


Fixture:getRestitution

Returns the restitution of the fixture.

Fixture:getRestitution()

| name | type | description |
| --- | --- | --- |
| restitution | number | The fixture restitution. |


Fixture:getShape

Returns the shape of the fixture. This shape is a reference to the actual data used in the simulation. It's possible to change its values between timesteps.

Fixture:getShape()

| name | type | description |
| --- | --- | --- |
| shape | Shape | The fixture's shape. |


Fixture:getUserData

Returns the Lua value associated with this fixture.

Fixture:getUserData()

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value associated with the fixture. |


Fixture:isDestroyed

Gets whether the Fixture is destroyed. Destroyed fixtures cannot be used.

Fixture:isDestroyed()

| name | type | description |
| --- | --- | --- |
| destroyed | boolean | Whether the Fixture is destroyed. |


Fixture:isSensor

Returns whether the fixture is a sensor.

Fixture:isSensor()

| name | type | description |
| --- | --- | --- |
| sensor | boolean | If the fixture is a sensor. |


Fixture:rayCast

Casts a ray against the shape of the fixture and returns the surface normal vector and the line position where the ray hit. If the ray missed the shape, nil will be returned.

The ray starts on the first point of the input line and goes towards the second point of the line. The fifth argument is the maximum distance the ray is going to travel as a scale factor of the input line length.

The childIndex parameter is used to specify which child of a parent shape, such as a ChainShape, will be ray casted. For ChainShapes, the index of 1 is the first edge on the chain. Ray casting a parent shape will only test the child specified so if you want to test every shape of the parent, you must loop through all of its children.

The world position of the impact can be calculated by multiplying the line vector with the third return value and adding it to the line starting point.

hitx, hity = x1 + (x2 - x1) * fraction, y1 + (y2 - y1) * fraction

Fixture:rayCast(x1, y1, x2, y2, maxFraction, childIndex)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the input line starting point. |
| y1 | number | The y position of the input line starting point. |
| x2 | number | The x position of the input line end point. |
| y2 | number | The y position of the input line end point. |
| maxFraction | number | Ray length parameter. |
| childIndex | number | The index of the child the ray gets cast against. |

| name | type | description |
| --- | --- | --- |
| xn | number | The x component of the normal vector of the edge where the ray hit the shape. |
| yn | number | The y component of the normal vector of the edge where the ray hit the shape. |
| fraction | number | The position on the input line where the intersection happened as a factor of the line length. |


Fixture:setCategory

Sets the categories the fixture belongs to. There can be up to 16 categories represented as a number from 1 to 16.

All fixture's default category is 1.

Fixture:setCategory(...)

| name | type | description |
| --- | --- | --- |
| ... | number | The categories. |


Fixture:setDensity

Sets the density of the fixture. Call Body:resetMassData if this needs to take effect immediately.

Fixture:setDensity(density)

| name | type | description |
| --- | --- | --- |
| density | number | The fixture density in kilograms per square meter. |


Fixture:setFilterData

Sets the filter data of the fixture.

Groups, categories, and mask can be used to define the collision behaviour of the fixture.

If two fixtures are in the same group they either always collide if the group is positive, or never collide if it's negative. If the group is zero or they do not match, then the contact filter checks if the fixtures select a category of the other fixture with their masks. The fixtures do not collide if that's not the case. If they do have each other's categories selected, the return value of the custom contact filter will be used. They always collide if none was set.

There can be up to 16 categories. Categories and masks are encoded as the bits of a 16-bit integer.

When created, prior to calling this function, all fixtures have category set to 1, mask set to 65535 (all categories) and group set to 0.

This function allows setting all filter data for a fixture at once. To set only the categories, the mask or the group, you can use Fixture:setCategory, Fixture:setMask or Fixture:setGroupIndex respectively.

Fixture:setFilterData(categories, mask, group)

| name | type | description |
| --- | --- | --- |
| categories | number | The categories as an integer from 0 to 65535. |
| mask | number | The mask as an integer from 0 to 65535. |
| group | number | The group as an integer from -32768 to 32767. |


Fixture:setFriction

Sets the friction of the fixture.

Friction determines how shapes react when they 'slide' along other shapes. Low friction indicates a slippery surface, like ice, while high friction indicates a rough surface, like concrete. Range: 0.0 - 1.0.

Fixture:setFriction(friction)

| name | type | description |
| --- | --- | --- |
| friction | number | The fixture friction. |


Fixture:setGroupIndex

Sets the group the fixture belongs to. Fixtures with the same group will always collide if the group is positive or never collide if it's negative. The group zero means no group.

The groups range from -32768 to 32767.

Fixture:setGroupIndex(group)

| name | type | description |
| --- | --- | --- |
| group | number | The group as an integer from -32768 to 32767. |


Fixture:setMask

Sets the category mask of the fixture. There can be up to 16 categories represented as a number from 1 to 16.

This fixture will '''NOT''' collide with the fixtures that are in the selected categories if the other fixture also has a category of this fixture selected.

Fixture:setMask(...)

| name | type | description |
| --- | --- | --- |
| ... | number | The masks. |


Fixture:setRestitution

Sets the restitution of the fixture.

Fixture:setRestitution(restitution)

| name | type | description |
| --- | --- | --- |
| restitution | number | The fixture restitution. |


Fixture:setSensor

Sets whether the fixture should act as a sensor.

Sensors do not cause collision responses, but the begin-contact and end-contact World callbacks will still be called for this fixture.

Fixture:setSensor(sensor)

| name | type | description |
| --- | --- | --- |
| sensor | boolean | The sensor status. |


Fixture:setUserData

Associates a Lua value with the fixture.

To delete the reference, explicitly pass nil.

Fixture:setUserData(value)

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value to associate with the fixture. |


Fixture:testPoint

Checks if a point is inside the shape of the fixture.

Fixture:testPoint(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the point. |
| y | number | The y position of the point. |

| name | type | description |
| --- | --- | --- |
| isInside | boolean | True if the point is inside or false if it is outside. |


Font:getAscent

Gets the ascent of the Font.

The ascent spans the distance between the baseline and the top of the glyph that reaches farthest from the baseline.

Font:getAscent()

| name | type | description |
| --- | --- | --- |
| ascent | number | The ascent of the Font in pixels. |


Font:getBaseline

Gets the baseline of the Font.

Most scripts share the notion of a baseline: an imaginary horizontal line on which characters rest. In some scripts, parts of glyphs lie below the baseline.

Font:getBaseline()

| name | type | description |
| --- | --- | --- |
| baseline | number | The baseline of the Font in pixels. |


Font:getDPIScale

Gets the DPI scale factor of the Font.

The DPI scale factor represents relative pixel density. A DPI scale factor of 2 means the font's glyphs have twice the pixel density in each dimension (4 times as many pixels in the same area) compared to a font with a DPI scale factor of 1.

The font size of TrueType fonts is scaled internally by the font's specified DPI scale factor. By default, LÖVE uses the screen's DPI scale factor when creating TrueType fonts.

Font:getDPIScale()

| name | type | description |
| --- | --- | --- |
| dpiscale | number | The DPI scale factor of the Font. |


Font:getDescent

Gets the descent of the Font.

The descent spans the distance between the baseline and the lowest descending glyph in a typeface.

Font:getDescent()

| name | type | description |
| --- | --- | --- |
| descent | number | The descent of the Font in pixels. |


Font:getFilter

Gets the filter mode for a font.

Font:getFilter()

| name | type | description |
| --- | --- | --- |
| min | FilterMode | Filter mode used when minifying the font. |
| mag | FilterMode | Filter mode used when magnifying the font. |
| anisotropy | number | Maximum amount of anisotropic filtering used. |


Font:getHeight

Gets the height of the Font.

The height of the font is the size including any spacing; the height which it will need.

Font:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the Font in pixels. |


Font:getKerning

Gets the kerning between two characters in the Font.

Kerning is normally handled automatically in love.graphics.print, Text objects, Font:getWidth, Font:getWrap, etc. This function is useful when stitching text together manually.

Font:getKerning(leftchar, rightchar)

| name | type | description |
| --- | --- | --- |
| leftchar | string | The left character. |
| rightchar | string | The right character. |

| name | type | description |
| --- | --- | --- |
| kerning | number | The kerning amount to add to the spacing between the two characters. May be negative. |

Font:getKerning(leftglyph, rightglyph)

| name | type | description |
| --- | --- | --- |
| leftglyph | number | The unicode number for the left glyph. |
| rightglyph | number | The unicode number for the right glyph. |

| name | type | description |
| --- | --- | --- |
| kerning | number | The kerning amount to add to the spacing between the two characters. May be negative. |


Font:getLineHeight

Gets the line height.

This will be the value previously set by Font:setLineHeight, or 1.0 by default.

Font:getLineHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The current line height. |


Font:getWidth

Determines the maximum width (accounting for newlines) taken by the given string.

Font:getWidth(text)

| name | type | description |
| --- | --- | --- |
| text | string | A string. |

| name | type | description |
| --- | --- | --- |
| width | number | The width of the text. |


Font:getWrap

Gets formatting information for text, given a wrap limit.

This function accounts for newlines correctly (i.e. '\n').

Font:getWrap(text, wraplimit)

| name | type | description |
| --- | --- | --- |
| text | string | The text that will be wrapped. |
| wraplimit | number | The maximum width in pixels of each line that ''text'' is allowed before wrapping. |

| name | type | description |
| --- | --- | --- |
| width | number | The maximum width of the wrapped text. |
| wrappedtext | table | A sequence containing each line of text that was wrapped. |

Font:getWrap(coloredtext, wraplimit)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| wraplimit | number | The maximum width in pixels of each line that ''text'' is allowed before wrapping. |

| name | type | description |
| --- | --- | --- |
| width | number | The maximum width of the wrapped text. |
| wrappedtext | table | A sequence containing each line of text that was wrapped. |


Font:hasGlyphs

Gets whether the Font can render a character or string.

Font:hasGlyphs(text)

| name | type | description |
| --- | --- | --- |
| text | string | A UTF-8 encoded unicode string. |

| name | type | description |
| --- | --- | --- |
| hasglyph | boolean | Whether the font can render all the UTF-8 characters in the string. |

Font:hasGlyphs(character1, character2)

| name | type | description |
| --- | --- | --- |
| character1 | string | A unicode character. |
| character2 | string | Another unicode character. |

| name | type | description |
| --- | --- | --- |
| hasglyph | boolean | Whether the font can render all the glyphs represented by the characters. |

Font:hasGlyphs(codepoint1, codepoint2)

| name | type | description |
| --- | --- | --- |
| codepoint1 | number | A unicode codepoint number. |
| codepoint2 | number | Another unicode codepoint number. |

| name | type | description |
| --- | --- | --- |
| hasglyph | boolean | Whether the font can render all the glyphs represented by the codepoint numbers. |


Font:setFallbacks

Sets the fallback fonts. When the Font doesn't contain a glyph, it will substitute the glyph from the next subsequent fallback Fonts. This is akin to setting a 'font stack' in Cascading Style Sheets (CSS).

Font:setFallbacks(fallbackfont1, ...)

| name | type | description |
| --- | --- | --- |
| fallbackfont1 | Font | The first fallback Font to use. |
| ... | Font | Additional fallback Fonts. |


Font:setFilter

Sets the filter mode for a font.

Font:setFilter(min, mag, anisotropy)

| name | type | description |
| --- | --- | --- |
| min | FilterMode | How to scale a font down. |
| mag | FilterMode | How to scale a font up. |
| anisotropy | number | Maximum amount of anisotropic filtering used. |


Font:setLineHeight

Sets the line height.

When rendering the font in lines the actual height will be determined by the line height multiplied by the height of the font. The default is 1.0.

Font:setLineHeight(height)

| name | type | description |
| --- | --- | --- |
| height | number | The new line height. |


FrictionJoint:getMaxForce

Gets the maximum friction force in Newtons.

FrictionJoint:getMaxForce()

| name | type | description |
| --- | --- | --- |
| force | number | Maximum force in Newtons. |


FrictionJoint:getMaxTorque

Gets the maximum friction torque in Newton-meters.

FrictionJoint:getMaxTorque()

| name | type | description |
| --- | --- | --- |
| torque | number | Maximum torque in Newton-meters. |


FrictionJoint:setMaxForce

Sets the maximum friction force in Newtons.

FrictionJoint:setMaxForce(maxForce)

| name | type | description |
| --- | --- | --- |
| maxForce | number | Max force in Newtons. |


FrictionJoint:setMaxTorque

Sets the maximum friction torque in Newton-meters.

FrictionJoint:setMaxTorque(torque)

| name | type | description |
| --- | --- | --- |
| torque | number | Maximum torque in Newton-meters. |


GearJoint:getJoints

Get the Joints connected by this GearJoint.

GearJoint:getJoints()

| name | type | description |
| --- | --- | --- |
| joint1 | Joint | The first connected Joint. |
| joint2 | Joint | The second connected Joint. |


GearJoint:getRatio

Get the ratio of a gear joint.

GearJoint:getRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The ratio of the joint. |


GearJoint:setRatio

Set the ratio of a gear joint.

GearJoint:setRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The new ratio of the joint. |


GlyphData:getAdvance

Gets glyph advance.

GlyphData:getAdvance()

| name | type | description |
| --- | --- | --- |
| advance | number | Glyph advance. |


GlyphData:getBearing

Gets glyph bearing.

GlyphData:getBearing()

| name | type | description |
| --- | --- | --- |
| bx | number | Glyph bearing X. |
| by | number | Glyph bearing Y. |


GlyphData:getBoundingBox

Gets glyph bounding box.

GlyphData:getBoundingBox()

| name | type | description |
| --- | --- | --- |
| x | number | Glyph position x. |
| y | number | Glyph position y. |
| width | number | Glyph width. |
| height | number | Glyph height. |


GlyphData:getDimensions

Gets glyph dimensions.

GlyphData:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | Glyph width. |
| height | number | Glyph height. |


GlyphData:getFormat

Gets glyph pixel format.

GlyphData:getFormat()

| name | type | description |
| --- | --- | --- |
| format | PixelFormat | Glyph pixel format. |


GlyphData:getGlyph

Gets glyph number.

GlyphData:getGlyph()

| name | type | description |
| --- | --- | --- |
| glyph | number | Glyph number. |


GlyphData:getGlyphString

Gets glyph string.

GlyphData:getGlyphString()

| name | type | description |
| --- | --- | --- |
| glyph | string | Glyph string. |


GlyphData:getHeight

Gets glyph height.

GlyphData:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | Glyph height. |


GlyphData:getWidth

Gets glyph width.

GlyphData:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | Glyph width. |


Image:isCompressed

Gets whether the Image was created from CompressedData.

Compressed images take up less space in VRAM, and drawing a compressed image will generally be more efficient than drawing one created from raw pixel data.

Image:isCompressed()

| name | type | description |
| --- | --- | --- |
| compressed | boolean | Whether the Image is stored as a compressed texture on the GPU. |


Image:isFormatLinear

Gets whether the Image was created with the linear (non-gamma corrected) flag set to true.

This method always returns false when gamma-correct rendering is not enabled.

Image:isFormatLinear()

| name | type | description |
| --- | --- | --- |
| linear | boolean | Whether the Image's internal pixel format is linear (not gamma corrected), when gamma-correct rendering is enabled. |


Image:replacePixels

Replace the contents of an Image.

Image:replacePixels(data, slice, mipmap, x, y, reloadmipmaps)

| name | type | description |
| --- | --- | --- |
| data | ImageData | The new ImageData to replace the contents with. |
| slice | number | Which cubemap face, array index, or volume layer to replace, if applicable. |
| mipmap | number | The mimap level to replace, if the Image has mipmaps. |
| x | number | The x-offset in pixels from the top-left of the image to replace. The given ImageData's width plus this value must not be greater than the pixel width of the Image's specified mipmap level. |
| y | number | The y-offset in pixels from the top-left of the image to replace. The given ImageData's height plus this value must not be greater than the pixel height of the Image's specified mipmap level. |
| reloadmipmaps | boolean | Whether to generate new mipmaps after replacing the Image's pixels. True by default if the Image was created with automatically generated mipmaps, false by default otherwise. |


ImageData:encode

Encodes the ImageData and optionally writes it to the save directory.

ImageData:encode(format, filename)

| name | type | description |
| --- | --- | --- |
| format | ImageFormat | The format to encode the image as. |
| filename | string | The filename to write the file to. If nil, no file will be written but the FileData will still be returned. |

| name | type | description |
| --- | --- | --- |
| filedata | FileData | The encoded image as a new FileData object. |

ImageData:encode(outFile)

| name | type | description |
| --- | --- | --- |
| outFile | string | Name of a file to write encoded data to. The format will be automatically deduced from the file extension. |

ImageData:encode(outFile, format)

| name | type | description |
| --- | --- | --- |
| outFile | string | Name of a file to write encoded data to. |
| format | ImageFormat | The format to encode the image in. |


ImageData:getDimensions

Gets the width and height of the ImageData in pixels.

ImageData:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the ImageData in pixels. |
| height | number | The height of the ImageData in pixels. |


ImageData:getFormat

Gets the pixel format of the ImageData.

ImageData:getFormat()

| name | type | description |
| --- | --- | --- |
| format | PixelFormat | The pixel format the ImageData was created with. |


ImageData:getHeight

Gets the height of the ImageData in pixels.

ImageData:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the ImageData in pixels. |


ImageData:getPixel

Gets the color of a pixel at a specific position in the image.

Valid x and y values start at 0 and go up to image width and height minus 1. Non-integer values are floored.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

ImageData:getPixel(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the pixel on the x-axis. |
| y | number | The position of the pixel on the y-axis. |

| name | type | description |
| --- | --- | --- |
| r | number | The red component (0-1). |
| g | number | The green component (0-1). |
| b | number | The blue component (0-1). |
| a | number | The alpha component (0-1). |


ImageData:getWidth

Gets the width of the ImageData in pixels.

ImageData:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the ImageData in pixels. |


ImageData:mapPixel

Transform an image by applying a function to every pixel.

This function is a higher-order function. It takes another function as a parameter, and calls it once for each pixel in the ImageData.

The passed function is called with six parameters for each pixel in turn. The parameters are numbers that represent the x and y coordinates of the pixel and its red, green, blue and alpha values. The function should return the new red, green, blue, and alpha values for that pixel.

function pixelFunction(x, y, r, g, b, a)

    -- template for defining your own pixel mapping function

    -- perform computations giving the new values for r, g, b and a

    -- ...

    return r, g, b, a

end

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

ImageData:mapPixel(pixelFunction, x, y, width, height)

| name | type | description |
| --- | --- | --- |
| pixelFunction | function | Function to apply to every pixel. |
| x | number | The x-axis of the top-left corner of the area within the ImageData to apply the function to. |
| y | number | The y-axis of the top-left corner of the area within the ImageData to apply the function to. |
| width | number | The width of the area within the ImageData to apply the function to. |
| height | number | The height of the area within the ImageData to apply the function to. |


ImageData:paste

Paste into ImageData from another source ImageData.

ImageData:paste(source, dx, dy, sx, sy, sw, sh)

| name | type | description |
| --- | --- | --- |
| source | ImageData | Source ImageData from which to copy. |
| dx | number | Destination top-left position on x-axis. |
| dy | number | Destination top-left position on y-axis. |
| sx | number | Source top-left position on x-axis. |
| sy | number | Source top-left position on y-axis. |
| sw | number | Source width. |
| sh | number | Source height. |


ImageData:setPixel

Sets the color of a pixel at a specific position in the image.

Valid x and y values start at 0 and go up to image width and height minus 1.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

ImageData:setPixel(x, y, r, g, b, a)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the pixel on the x-axis. |
| y | number | The position of the pixel on the y-axis. |
| r | number | The red component (0-1). |
| g | number | The green component (0-1). |
| b | number | The blue component (0-1). |
| a | number | The alpha component (0-1). |

ImageData:setPixel(x, y, color)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the pixel on the x-axis. |
| y | number | The position of the pixel on the y-axis. |
| color | table | A numerical indexed table with the red, green, blue and alpha values as numbers. |


Joint:destroy

Explicitly destroys the Joint. An error will occur if you attempt to use the object after calling this function.

In 0.7.2, when you don't have time to wait for garbage collection, this function

may be used to free the object immediately.

Joint:destroy()


Joint:getAnchors

Get the anchor points of the joint.

Joint:getAnchors()

| name | type | description |
| --- | --- | --- |
| x1 | number | The x-component of the anchor on Body 1. |
| y1 | number | The y-component of the anchor on Body 1. |
| x2 | number | The x-component of the anchor on Body 2. |
| y2 | number | The y-component of the anchor on Body 2. |


Joint:getBodies

Gets the bodies that the Joint is attached to.

Joint:getBodies()

| name | type | description |
| --- | --- | --- |
| bodyA | Body | The first Body. |
| bodyB | Body | The second Body. |


Joint:getCollideConnected

Gets whether the connected Bodies collide.

Joint:getCollideConnected()

| name | type | description |
| --- | --- | --- |
| c | boolean | True if they collide, false otherwise. |


Joint:getReactionForce

Returns the reaction force in newtons on the second body

Joint:getReactionForce(x)

| name | type | description |
| --- | --- | --- |
| x | number | How long the force applies. Usually the inverse time step or 1/dt. |

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the force. |
| y | number | The y-component of the force. |


Joint:getReactionTorque

Returns the reaction torque on the second body.

Joint:getReactionTorque(invdt)

| name | type | description |
| --- | --- | --- |
| invdt | number | How long the force applies. Usually the inverse time step or 1/dt. |

| name | type | description |
| --- | --- | --- |
| torque | number | The reaction torque on the second body. |


Joint:getType

Gets a string representing the type.

Joint:getType()

| name | type | description |
| --- | --- | --- |
| type | JointType | A string with the name of the Joint type. |


Joint:getUserData

Returns the Lua value associated with this Joint.

Joint:getUserData()

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value associated with the Joint. |


Joint:isDestroyed

Gets whether the Joint is destroyed. Destroyed joints cannot be used.

Joint:isDestroyed()

| name | type | description |
| --- | --- | --- |
| destroyed | boolean | Whether the Joint is destroyed. |


Joint:setUserData

Associates a Lua value with the Joint.

To delete the reference, explicitly pass nil.

Joint:setUserData(value)

| name | type | description |
| --- | --- | --- |
| value | any | The Lua value to associate with the Joint. |


Joystick:getAxes

Gets the direction of each axis.

Joystick:getAxes()

| name | type | description |
| --- | --- | --- |
| axisDir1 | number | Direction of axis1. |
| axisDir2 | number | Direction of axis2. |
| axisDirN | number | Direction of axisN. |


Joystick:getAxis

Gets the direction of an axis.

Joystick:getAxis(axis)

| name | type | description |
| --- | --- | --- |
| axis | number | The index of the axis to be checked. |

| name | type | description |
| --- | --- | --- |
| direction | number | Current value of the axis. |


Joystick:getAxisCount

Gets the number of axes on the joystick.

Joystick:getAxisCount()

| name | type | description |
| --- | --- | --- |
| axes | number | The number of axes available. |


Joystick:getButtonCount

Gets the number of buttons on the joystick.

Joystick:getButtonCount()

| name | type | description |
| --- | --- | --- |
| buttons | number | The number of buttons available. |


Joystick:getDeviceInfo

Gets the USB vendor ID, product ID, and product version numbers of joystick which consistent across operating systems.

Can be used to show different icons, etc. for different gamepads.

Joystick:getDeviceInfo()

| name | type | description |
| --- | --- | --- |
| vendorID | number | The USB vendor ID of the joystick. |
| productID | number | The USB product ID of the joystick. |
| productVersion | number | The product version of the joystick. |


Joystick:getGUID

Gets a stable GUID unique to the type of the physical joystick which does not change over time. For example, all Sony Dualshock 3 controllers in OS X have the same GUID. The value is platform-dependent.

Joystick:getGUID()

| name | type | description |
| --- | --- | --- |
| guid | string | The Joystick type's OS-dependent unique identifier. |


Joystick:getGamepadAxis

Gets the direction of a virtual gamepad axis. If the Joystick isn't recognized as a gamepad or isn't connected, this function will always return 0.

Joystick:getGamepadAxis(axis)

| name | type | description |
| --- | --- | --- |
| axis | GamepadAxis | The virtual axis to be checked. |

| name | type | description |
| --- | --- | --- |
| direction | number | Current value of the axis. |


Joystick:getGamepadMapping

Gets the button, axis or hat that a virtual gamepad input is bound to.

Joystick:getGamepadMapping(axis)

| name | type | description |
| --- | --- | --- |
| axis | GamepadAxis | The virtual gamepad axis to get the binding for. |

| name | type | description |
| --- | --- | --- |
| inputtype | JoystickInputType | The type of input the virtual gamepad axis is bound to. |
| inputindex | number | The index of the Joystick's button, axis or hat that the virtual gamepad axis is bound to. |
| hatdirection | JoystickHat | The direction of the hat, if the virtual gamepad axis is bound to a hat. nil otherwise. |

Joystick:getGamepadMapping(button)

| name | type | description |
| --- | --- | --- |
| button | GamepadButton | The virtual gamepad button to get the binding for. |

| name | type | description |
| --- | --- | --- |
| inputtype | JoystickInputType | The type of input the virtual gamepad button is bound to. |
| inputindex | number | The index of the Joystick's button, axis or hat that the virtual gamepad button is bound to. |
| hatdirection | JoystickHat | The direction of the hat, if the virtual gamepad button is bound to a hat. nil otherwise. |


Joystick:getGamepadMappingString

Gets the full gamepad mapping string of this Joystick, or nil if it's not recognized as a gamepad.

The mapping string contains binding information used to map the Joystick's buttons an axes to the standard gamepad layout, and can be used later with love.joystick.loadGamepadMappings.

Joystick:getGamepadMappingString()

| name | type | description |
| --- | --- | --- |
| mappingstring | string | A string containing the Joystick's gamepad mappings, or nil if the Joystick is not recognized as a gamepad. |


Joystick:getHat

Gets the direction of the Joystick's hat.

Joystick:getHat(hat)

| name | type | description |
| --- | --- | --- |
| hat | number | The index of the hat to be checked. |

| name | type | description |
| --- | --- | --- |
| direction | JoystickHat | The direction the hat is pushed. |


Joystick:getHatCount

Gets the number of hats on the joystick.

Joystick:getHatCount()

| name | type | description |
| --- | --- | --- |
| hats | number | How many hats the joystick has. |


Joystick:getID

Gets the joystick's unique identifier. The identifier will remain the same for the life of the game, even when the Joystick is disconnected and reconnected, but it '''will''' change when the game is re-launched.

Joystick:getID()

| name | type | description |
| --- | --- | --- |
| id | number | The Joystick's unique identifier. Remains the same as long as the game is running. |
| instanceid | number | Unique instance identifier. Changes every time the Joystick is reconnected. nil if the Joystick is not connected. |


Joystick:getName

Gets the name of the joystick.

Joystick:getName()

| name | type | description |
| --- | --- | --- |
| name | string | The name of the joystick. |


Joystick:getVibration

Gets the current vibration motor strengths on a Joystick with rumble support.

Joystick:getVibration()

| name | type | description |
| --- | --- | --- |
| left | number | Current strength of the left vibration motor on the Joystick. |
| right | number | Current strength of the right vibration motor on the Joystick. |


Joystick:isConnected

Gets whether the Joystick is connected.

Joystick:isConnected()

| name | type | description |
| --- | --- | --- |
| connected | boolean | True if the Joystick is currently connected, false otherwise. |


Joystick:isDown

Checks if a button on the Joystick is pressed.

LÖVE 0.9.0 had a bug which required the button indices passed to Joystick:isDown to be 0-based instead of 1-based, for example button 1 would be 0 for this function. It was fixed in 0.9.1.

Joystick:isDown(buttonN)

| name | type | description |
| --- | --- | --- |
| buttonN | number | The index of a button to check. |

| name | type | description |
| --- | --- | --- |
| anyDown | boolean | True if any supplied button is down, false if not. |


Joystick:isGamepad

Gets whether the Joystick is recognized as a gamepad. If this is the case, the Joystick's buttons and axes can be used in a standardized manner across different operating systems and joystick models via Joystick:getGamepadAxis, Joystick:isGamepadDown, love.gamepadpressed, and related functions.

LÖVE automatically recognizes most popular controllers with a similar layout to the Xbox 360 controller as gamepads, but you can add more with love.joystick.setGamepadMapping.

Joystick:isGamepad()

| name | type | description |
| --- | --- | --- |
| isgamepad | boolean | True if the Joystick is recognized as a gamepad, false otherwise. |


Joystick:isGamepadDown

Checks if a virtual gamepad button on the Joystick is pressed. If the Joystick is not recognized as a Gamepad or isn't connected, then this function will always return false.

Joystick:isGamepadDown(buttonN)

| name | type | description |
| --- | --- | --- |
| buttonN | GamepadButton | The gamepad button to check. |

| name | type | description |
| --- | --- | --- |
| anyDown | boolean | True if any supplied button is down, false if not. |


Joystick:isVibrationSupported

Gets whether the Joystick supports vibration.

Joystick:isVibrationSupported()

| name | type | description |
| --- | --- | --- |
| supported | boolean | True if rumble / force feedback vibration is supported on this Joystick, false if not. |


Joystick:setVibration

Sets the vibration motor speeds on a Joystick with rumble support. Most common gamepads have this functionality, although not all drivers give proper support. Use Joystick:isVibrationSupported to check.

Joystick:setVibration(left, right)

| name | type | description |
| --- | --- | --- |
| left | number | Strength of the left vibration motor on the Joystick. Must be in the range of 1. |
| right | number | Strength of the right vibration motor on the Joystick. Must be in the range of 1. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the vibration was successfully applied, false if not. |

Joystick:setVibration()

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the vibration was successfully disabled, false if not. |

Joystick:setVibration(left, right, duration)

| name | type | description |
| --- | --- | --- |
| left | number | Strength of the left vibration motor on the Joystick. Must be in the range of 1. |
| right | number | Strength of the right vibration motor on the Joystick. Must be in the range of 1. |
| duration | number | The duration of the vibration in seconds. A negative value means infinite duration. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the vibration was successfully applied, false if not. |


Mesh:attachAttribute

Attaches a vertex attribute from a different Mesh onto this Mesh, for use when drawing. This can be used to share vertex attribute data between several different Meshes.

Mesh:attachAttribute(name, mesh)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the vertex attribute to attach. |
| mesh | Mesh | The Mesh to get the vertex attribute from. |

Mesh:attachAttribute(name, mesh, step, attachname)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the vertex attribute to attach. |
| mesh | Mesh | The Mesh to get the vertex attribute from. |
| step | VertexAttributeStep | Whether the attribute will be per-vertex or per-instance when the mesh is drawn. |
| attachname | string | The name of the attribute to use in shader code. Defaults to the name of the attribute in the given mesh. Can be used to use a different name for this attribute when rendering. |


Mesh:detachAttribute

Removes a previously attached vertex attribute from this Mesh.

Mesh:detachAttribute(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the attached vertex attribute to detach. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the attribute was successfully detached. |


Mesh:flush

Immediately sends all modified vertex data in the Mesh to the graphics card.

Normally it isn't necessary to call this method as love.graphics.draw(mesh, ...) will do it automatically if needed, but explicitly using **Mesh:flush** gives more control over when the work happens.

If this method is used, it generally shouldn't be called more than once (at most) between love.graphics.draw(mesh, ...) calls.

Mesh:flush()


Mesh:getDrawMode

Gets the mode used when drawing the Mesh.

Mesh:getDrawMode()

| name | type | description |
| --- | --- | --- |
| mode | MeshDrawMode | The mode used when drawing the Mesh. |


Mesh:getDrawRange

Gets the range of vertices used when drawing the Mesh.

Mesh:getDrawRange()

| name | type | description |
| --- | --- | --- |
| min | number | The index of the first vertex used when drawing, or the index of the first value in the vertex map used if one is set for this Mesh. |
| max | number | The index of the last vertex used when drawing, or the index of the last value in the vertex map used if one is set for this Mesh. |


Mesh:getTexture

Gets the texture (Image or Canvas) used when drawing the Mesh.

Mesh:getTexture()

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Image or Canvas to texture the Mesh with when drawing, or nil if none is set. |


Mesh:getVertex

Gets the properties of a vertex in the Mesh.

In versions prior to 11.0, color and byte component values were within the range of 0 to 255 instead of 0 to 1.

Mesh:getVertex(index)

| name | type | description |
| --- | --- | --- |
| index | number | The one-based index of the vertex you want to retrieve the information for. |

| name | type | description |
| --- | --- | --- |
| attributecomponent | number | The first component of the first vertex attribute in the specified vertex. |
| ... | number | Additional components of all vertex attributes in the specified vertex. |

Mesh:getVertex(index)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the vertex you want to retrieve the information for. |

| name | type | description |
| --- | --- | --- |
| x | number | The position of the vertex on the x-axis. |
| y | number | The position of the vertex on the y-axis. |
| u | number | The horizontal component of the texture coordinate. |
| v | number | The vertical component of the texture coordinate. |
| r | number | The red component of the vertex's color. |
| g | number | The green component of the vertex's color. |
| b | number | The blue component of the vertex's color. |
| a | number | The alpha component of the vertex's color. |


Mesh:getVertexAttribute

Gets the properties of a specific attribute within a vertex in the Mesh.

Meshes without a custom vertex format specified in love.graphics.newMesh have position as their first attribute, texture coordinates as their second attribute, and color as their third attribute.

Mesh:getVertexAttribute(vertexindex, attributeindex)

| name | type | description |
| --- | --- | --- |
| vertexindex | number | The index of the the vertex you want to retrieve the attribute for (one-based). |
| attributeindex | number | The index of the attribute within the vertex to be retrieved (one-based). |

| name | type | description |
| --- | --- | --- |
| value1 | number | The value of the first component of the attribute. |
| value2 | number | The value of the second component of the attribute. |
| ... | number | Any additional vertex attribute components. |


Mesh:getVertexCount

Gets the total number of vertices in the Mesh.

Mesh:getVertexCount()

| name | type | description |
| --- | --- | --- |
| count | number | The total number of vertices in the mesh. |


Mesh:getVertexFormat

Gets the vertex format that the Mesh was created with.

Mesh:getVertexFormat()

| name | type | description |
| --- | --- | --- |
| format | table | The vertex format of the Mesh, which is a table containing tables for each vertex attribute the Mesh was created with, in the form of {attribute, ...}. |


Mesh:getVertexMap

Gets the vertex map for the Mesh. The vertex map describes the order in which the vertices are used when the Mesh is drawn. The vertices, vertex map, and mesh draw mode work together to determine what exactly is displayed on the screen.

If no vertex map has been set previously via Mesh:setVertexMap, then this function will return nil in LÖVE 0.10.0+, or an empty table in 0.9.2 and older.

Mesh:getVertexMap()

| name | type | description |
| --- | --- | --- |
| map | table | A table containing the list of vertex indices used when drawing. |


Mesh:isAttributeEnabled

Gets whether a specific vertex attribute in the Mesh is enabled. Vertex data from disabled attributes is not used when drawing the Mesh.

Mesh:isAttributeEnabled(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the vertex attribute to be checked. |

| name | type | description |
| --- | --- | --- |
| enabled | boolean | Whether the vertex attribute is used when drawing this Mesh. |


Mesh:setAttributeEnabled

Enables or disables a specific vertex attribute in the Mesh. Vertex data from disabled attributes is not used when drawing the Mesh.

Mesh:setAttributeEnabled(name, enable)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the vertex attribute to enable or disable. |
| enable | boolean | Whether the vertex attribute is used when drawing this Mesh. |


Mesh:setDrawMode

Sets the mode used when drawing the Mesh.

Mesh:setDrawMode(mode)

| name | type | description |
| --- | --- | --- |
| mode | MeshDrawMode | The mode to use when drawing the Mesh. |


Mesh:setDrawRange

Restricts the drawn vertices of the Mesh to a subset of the total.

Mesh:setDrawRange(start, count)

| name | type | description |
| --- | --- | --- |
| start | number | The index of the first vertex to use when drawing, or the index of the first value in the vertex map to use if one is set for this Mesh. |
| count | number | The number of vertices to use when drawing, or number of values in the vertex map to use if one is set for this Mesh. |

Mesh:setDrawRange()


Mesh:setTexture

Sets the texture (Image or Canvas) used when drawing the Mesh.

Mesh:setTexture(texture)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Image or Canvas to texture the Mesh with when drawing. |

Mesh:setTexture()


Mesh:setVertex

Sets the properties of a vertex in the Mesh.

In versions prior to 11.0, color and byte component values were within the range of 0 to 255 instead of 0 to 1.

Mesh:setVertex(index, attributecomponent, ...)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the the vertex you want to modify (one-based). |
| attributecomponent | number | The first component of the first vertex attribute in the specified vertex. |
| ... | number | Additional components of all vertex attributes in the specified vertex. |

Mesh:setVertex(index, vertex)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the the vertex you want to modify (one-based). |
| vertex | table | A table with vertex information, in the form of {attributecomponent, ...}. |

Mesh:setVertex(index, x, y, u, v, r, g, b, a)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the the vertex you want to modify (one-based). |
| x | number | The position of the vertex on the x-axis. |
| y | number | The position of the vertex on the y-axis. |
| u | number | The horizontal component of the texture coordinate. |
| v | number | The vertical component of the texture coordinate. |
| r | number | The red component of the vertex's color. |
| g | number | The green component of the vertex's color. |
| b | number | The blue component of the vertex's color. |
| a | number | The alpha component of the vertex's color. |

Mesh:setVertex(index, vertex)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the the vertex you want to modify (one-based). |
| vertex | table | A table with vertex information. |


Mesh:setVertexAttribute

Sets the properties of a specific attribute within a vertex in the Mesh.

Meshes without a custom vertex format specified in love.graphics.newMesh have position as their first attribute, texture coordinates as their second attribute, and color as their third attribute.

Mesh:setVertexAttribute(vertexindex, attributeindex, value1, value2, ...)

| name | type | description |
| --- | --- | --- |
| vertexindex | number | The index of the the vertex to be modified (one-based). |
| attributeindex | number | The index of the attribute within the vertex to be modified (one-based). |
| value1 | number | The new value for the first component of the attribute. |
| value2 | number | The new value for the second component of the attribute. |
| ... | number | Any additional vertex attribute components. |


Mesh:setVertexMap

Sets the vertex map for the Mesh. The vertex map describes the order in which the vertices are used when the Mesh is drawn. The vertices, vertex map, and mesh draw mode work together to determine what exactly is displayed on the screen.

The vertex map allows you to re-order or reuse vertices when drawing without changing the actual vertex parameters or duplicating vertices. It is especially useful when combined with different Mesh Draw Modes.

Mesh:setVertexMap(map)

| name | type | description |
| --- | --- | --- |
| map | table | A table containing a list of vertex indices to use when drawing. Values must be in the range of Mesh:getVertexCount(). |

Mesh:setVertexMap(vi1, vi2, vi3)

| name | type | description |
| --- | --- | --- |
| vi1 | number | The index of the first vertex to use when drawing. Must be in the range of Mesh:getVertexCount(). |
| vi2 | number | The index of the second vertex to use when drawing. |
| vi3 | number | The index of the third vertex to use when drawing. |

Mesh:setVertexMap(data, datatype)

| name | type | description |
| --- | --- | --- |
| data | Data | Array of vertex indices to use when drawing. Values must be in the range of Mesh:getVertexCount()-1 |
| datatype | IndexDataType | Datatype of the vertex indices array above. |


Mesh:setVertices

Replaces a range of vertices in the Mesh with new ones. The total number of vertices in a Mesh cannot be changed after it has been created. This is often more efficient than calling Mesh:setVertex in a loop.

Mesh:setVertices(vertices, startvertex, count)

| name | type | description |
| --- | --- | --- |
| vertices | table | The table filled with vertex information tables for each vertex, in the form of {vertex, ...} where each vertex is a table in the form of {attributecomponent, ...}. |
| startvertex | number | The index of the first vertex to replace. |
| count | number | Amount of vertices to replace. |

Mesh:setVertices(data, startvertex)

| name | type | description |
| --- | --- | --- |
| data | Data | A Data object to copy from. The contents of the Data must match the layout of this Mesh's vertex format. |
| startvertex | number | The index of the first vertex to replace. |

Mesh:setVertices(vertices)

| name | type | description |
| --- | --- | --- |
| vertices | table | The table filled with vertex information tables for each vertex as follows: |


MotorJoint:getAngularOffset

Gets the target angular offset between the two Bodies the Joint is attached to.

MotorJoint:getAngularOffset()

| name | type | description |
| --- | --- | --- |
| angleoffset | number | The target angular offset in radians: the second body's angle minus the first body's angle. |


MotorJoint:getLinearOffset

Gets the target linear offset between the two Bodies the Joint is attached to.

MotorJoint:getLinearOffset()

| name | type | description |
| --- | --- | --- |
| x | number | The x component of the target linear offset, relative to the first Body. |
| y | number | The y component of the target linear offset, relative to the first Body. |


MotorJoint:setAngularOffset

Sets the target angluar offset between the two Bodies the Joint is attached to.

MotorJoint:setAngularOffset(angleoffset)

| name | type | description |
| --- | --- | --- |
| angleoffset | number | The target angular offset in radians: the second body's angle minus the first body's angle. |


MotorJoint:setLinearOffset

Sets the target linear offset between the two Bodies the Joint is attached to.

MotorJoint:setLinearOffset(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x component of the target linear offset, relative to the first Body. |
| y | number | The y component of the target linear offset, relative to the first Body. |


MouseJoint:getDampingRatio

Returns the damping ratio.

MouseJoint:getDampingRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The new damping ratio. |


MouseJoint:getFrequency

Returns the frequency.

MouseJoint:getFrequency()

| name | type | description |
| --- | --- | --- |
| freq | number | The frequency in hertz. |


MouseJoint:getMaxForce

Gets the highest allowed force.

MouseJoint:getMaxForce()

| name | type | description |
| --- | --- | --- |
| f | number | The max allowed force. |


MouseJoint:getTarget

Gets the target point.

MouseJoint:getTarget()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the target. |
| y | number | The x-component of the target. |


MouseJoint:setDampingRatio

Sets a new damping ratio.

MouseJoint:setDampingRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The new damping ratio. |


MouseJoint:setFrequency

Sets a new frequency.

MouseJoint:setFrequency(freq)

| name | type | description |
| --- | --- | --- |
| freq | number | The new frequency in hertz. |


MouseJoint:setMaxForce

Sets the highest allowed force.

MouseJoint:setMaxForce(f)

| name | type | description |
| --- | --- | --- |
| f | number | The max allowed force. |


MouseJoint:setTarget

Sets the target point.

MouseJoint:setTarget(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the target. |
| y | number | The y-component of the target. |


Object:release

Destroys the object's Lua reference. The object will be completely deleted if it's not referenced by any other LÖVE object or thread.

This method can be used to immediately clean up resources without waiting for Lua's garbage collector.

Object:release()

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the object was released by this call, false if it had been previously released. |


Object:type

Gets the type of the object as a string.

Object:type()

| name | type | description |
| --- | --- | --- |
| type | string | The type as a string. |


Object:typeOf

Checks whether an object is of a certain type. If the object has the type with the specified name in its hierarchy, this function will return true.

Object:typeOf(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the type to check for. |

| name | type | description |
| --- | --- | --- |
| b | boolean | True if the object is of the specified type, false otherwise. |


ParticleSystem:clone

Creates an identical copy of the ParticleSystem in the stopped state.

ParticleSystem:clone()

| name | type | description |
| --- | --- | --- |
| particlesystem | ParticleSystem | The new identical copy of this ParticleSystem. |


ParticleSystem:emit

Emits a burst of particles from the particle emitter.

ParticleSystem:emit(numparticles)

| name | type | description |
| --- | --- | --- |
| numparticles | number | The amount of particles to emit. The number of emitted particles will be truncated if the particle system's max buffer size is reached. |


ParticleSystem:getBufferSize

Gets the maximum number of particles the ParticleSystem can have at once.

ParticleSystem:getBufferSize()

| name | type | description |
| --- | --- | --- |
| size | number | The maximum number of particles. |


ParticleSystem:getColors

Gets the series of colors applied to the particle sprite.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

ParticleSystem:getColors()

| name | type | description |
| --- | --- | --- |
| r1 | number | First color, red component (0-1). |
| g1 | number | First color, green component (0-1). |
| b1 | number | First color, blue component (0-1). |
| a1 | number | First color, alpha component (0-1). |
| r2 | number | Second color, red component (0-1). |
| g2 | number | Second color, green component (0-1). |
| b2 | number | Second color, blue component (0-1). |
| a2 | number | Second color, alpha component (0-1). |
| r8 | number | Eighth color, red component (0-1). |
| g8 | number | Eighth color, green component (0-1). |
| b8 | number | Eighth color, blue component (0-1). |
| a8 | number | Eighth color, alpha component (0-1). |


ParticleSystem:getCount

Gets the number of particles that are currently in the system.

ParticleSystem:getCount()

| name | type | description |
| --- | --- | --- |
| count | number | The current number of live particles. |


ParticleSystem:getDirection

Gets the direction of the particle emitter (in radians).

ParticleSystem:getDirection()

| name | type | description |
| --- | --- | --- |
| direction | number | The direction of the emitter (radians). |


ParticleSystem:getEmissionArea

Gets the area-based spawn parameters for the particles.

ParticleSystem:getEmissionArea()

| name | type | description |
| --- | --- | --- |
| distribution | AreaSpreadDistribution | The type of distribution for new particles. |
| dx | number | The maximum spawn distance from the emitter along the x-axis for uniform distribution, or the standard deviation along the x-axis for normal distribution. |
| dy | number | The maximum spawn distance from the emitter along the y-axis for uniform distribution, or the standard deviation along the y-axis for normal distribution. |
| angle | number | The angle in radians of the emission area. |
| directionRelativeToCenter | boolean | True if newly spawned particles will be oriented relative to the center of the emission area, false otherwise. |


ParticleSystem:getEmissionRate

Gets the amount of particles emitted per second.

ParticleSystem:getEmissionRate()

| name | type | description |
| --- | --- | --- |
| rate | number | The amount of particles per second. |


ParticleSystem:getEmitterLifetime

Gets how long the particle system will emit particles (if -1 then it emits particles forever).

ParticleSystem:getEmitterLifetime()

| name | type | description |
| --- | --- | --- |
| life | number | The lifetime of the emitter (in seconds). |


ParticleSystem:getInsertMode

Gets the mode used when the ParticleSystem adds new particles.

ParticleSystem:getInsertMode()

| name | type | description |
| --- | --- | --- |
| mode | ParticleInsertMode | The mode used when the ParticleSystem adds new particles. |


ParticleSystem:getLinearAcceleration

Gets the linear acceleration (acceleration along the x and y axes) for particles.

Every particle created will accelerate along the x and y axes between xmin,ymin and xmax,ymax.

ParticleSystem:getLinearAcceleration()

| name | type | description |
| --- | --- | --- |
| xmin | number | The minimum acceleration along the x axis. |
| ymin | number | The minimum acceleration along the y axis. |
| xmax | number | The maximum acceleration along the x axis. |
| ymax | number | The maximum acceleration along the y axis. |


ParticleSystem:getLinearDamping

Gets the amount of linear damping (constant deceleration) for particles.

ParticleSystem:getLinearDamping()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum amount of linear damping applied to particles. |
| max | number | The maximum amount of linear damping applied to particles. |


ParticleSystem:getOffset

Gets the particle image's draw offset.

ParticleSystem:getOffset()

| name | type | description |
| --- | --- | --- |
| ox | number | The x coordinate of the particle image's draw offset. |
| oy | number | The y coordinate of the particle image's draw offset. |


ParticleSystem:getParticleLifetime

Gets the lifetime of the particles.

ParticleSystem:getParticleLifetime()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum life of the particles (in seconds). |
| max | number | The maximum life of the particles (in seconds). |


ParticleSystem:getPosition

Gets the position of the emitter.

ParticleSystem:getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | Position along x-axis. |
| y | number | Position along y-axis. |


ParticleSystem:getQuads

Gets the series of Quads used for the particle sprites.

ParticleSystem:getQuads()

| name | type | description |
| --- | --- | --- |
| quads | table | A table containing the Quads used. |


ParticleSystem:getRadialAcceleration

Gets the radial acceleration (away from the emitter).

ParticleSystem:getRadialAcceleration()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum acceleration. |
| max | number | The maximum acceleration. |


ParticleSystem:getRotation

Gets the rotation of the image upon particle creation (in radians).

ParticleSystem:getRotation()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum initial angle (radians). |
| max | number | The maximum initial angle (radians). |


ParticleSystem:getSizeVariation

Gets the amount of size variation (0 meaning no variation and 1 meaning full variation between start and end).

ParticleSystem:getSizeVariation()

| name | type | description |
| --- | --- | --- |
| variation | number | The amount of variation (0 meaning no variation and 1 meaning full variation between start and end). |


ParticleSystem:getSizes

Gets the series of sizes by which the sprite is scaled. 1.0 is normal size. The particle system will interpolate between each size evenly over the particle's lifetime.

ParticleSystem:getSizes()

| name | type | description |
| --- | --- | --- |
| size1 | number | The first size. |
| size2 | number | The second size. |
| size8 | number | The eighth size. |


ParticleSystem:getSpeed

Gets the speed of the particles.

ParticleSystem:getSpeed()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum linear speed of the particles. |
| max | number | The maximum linear speed of the particles. |


ParticleSystem:getSpin

Gets the spin of the sprite.

ParticleSystem:getSpin()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum spin (radians per second). |
| max | number | The maximum spin (radians per second). |
| variation | number | The degree of variation (0 meaning no variation and 1 meaning full variation between start and end). |


ParticleSystem:getSpinVariation

Gets the amount of spin variation (0 meaning no variation and 1 meaning full variation between start and end).

ParticleSystem:getSpinVariation()

| name | type | description |
| --- | --- | --- |
| variation | number | The amount of variation (0 meaning no variation and 1 meaning full variation between start and end). |


ParticleSystem:getSpread

Gets the amount of directional spread of the particle emitter (in radians).

ParticleSystem:getSpread()

| name | type | description |
| --- | --- | --- |
| spread | number | The spread of the emitter (radians). |


ParticleSystem:getTangentialAcceleration

Gets the tangential acceleration (acceleration perpendicular to the particle's direction).

ParticleSystem:getTangentialAcceleration()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum acceleration. |
| max | number | The maximum acceleration. |


ParticleSystem:getTexture

Gets the texture (Image or Canvas) used for the particles.

ParticleSystem:getTexture()

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Image or Canvas used for the particles. |


ParticleSystem:hasRelativeRotation

Gets whether particle angles and rotations are relative to their velocities. If enabled, particles are aligned to the angle of their velocities and rotate relative to that angle.

ParticleSystem:hasRelativeRotation()

| name | type | description |
| --- | --- | --- |
| enable | boolean | True if relative particle rotation is enabled, false if it's disabled. |


ParticleSystem:isActive

Checks whether the particle system is actively emitting particles.

ParticleSystem:isActive()

| name | type | description |
| --- | --- | --- |
| active | boolean | True if system is active, false otherwise. |


ParticleSystem:isPaused

Checks whether the particle system is paused.

ParticleSystem:isPaused()

| name | type | description |
| --- | --- | --- |
| paused | boolean | True if system is paused, false otherwise. |


ParticleSystem:isStopped

Checks whether the particle system is stopped.

ParticleSystem:isStopped()

| name | type | description |
| --- | --- | --- |
| stopped | boolean | True if system is stopped, false otherwise. |


ParticleSystem:moveTo

Moves the position of the emitter. This results in smoother particle spawning behaviour than if ParticleSystem:setPosition is used every frame.

ParticleSystem:moveTo(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | Position along x-axis. |
| y | number | Position along y-axis. |


ParticleSystem:pause

Pauses the particle emitter.

ParticleSystem:pause()


ParticleSystem:reset

Resets the particle emitter, removing any existing particles and resetting the lifetime counter.

ParticleSystem:reset()


ParticleSystem:setBufferSize

Sets the size of the buffer (the max allowed amount of particles in the system).

ParticleSystem:setBufferSize(size)

| name | type | description |
| --- | --- | --- |
| size | number | The buffer size. |


ParticleSystem:setColors

Sets a series of colors to apply to the particle sprite. The particle system will interpolate between each color evenly over the particle's lifetime.

Arguments can be passed in groups of four, representing the components of the desired RGBA value, or as tables of RGBA component values, with a default alpha value of 1 if only three values are given. At least one color must be specified. A maximum of eight may be used.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

ParticleSystem:setColors(r1, g1, b1, a1, ...)

| name | type | description |
| --- | --- | --- |
| r1 | number | First color, red component (0-1). |
| g1 | number | First color, green component (0-1). |
| b1 | number | First color, blue component (0-1). |
| a1 | number | First color, alpha component (0-1). |
| ... | number | Additional colors. |

ParticleSystem:setColors(rgba1, ...)

| name | type | description |
| --- | --- | --- |
| rgba1 | table | First color, a numerical indexed table with the red, green, blue and alpha values as numbers (0-1). The alpha is optional and defaults to 1 if it is left out. |
| ... | table | Additional color, a numerical indexed table with the red, green, blue and alpha values as numbers (0-1). The alpha is optional and defaults to 1 if it is left out. |


ParticleSystem:setDirection

Sets the direction the particles will be emitted in.

ParticleSystem:setDirection(direction)

| name | type | description |
| --- | --- | --- |
| direction | number | The direction of the particles (in radians). |


ParticleSystem:setEmissionArea

Sets area-based spawn parameters for the particles. Newly created particles will spawn in an area around the emitter based on the parameters to this function.

ParticleSystem:setEmissionArea(distribution, dx, dy, angle, directionRelativeToCenter)

| name | type | description |
| --- | --- | --- |
| distribution | AreaSpreadDistribution | The type of distribution for new particles. |
| dx | number | The maximum spawn distance from the emitter along the x-axis for uniform distribution, or the standard deviation along the x-axis for normal distribution. |
| dy | number | The maximum spawn distance from the emitter along the y-axis for uniform distribution, or the standard deviation along the y-axis for normal distribution. |
| angle | number | The angle in radians of the emission area. |
| directionRelativeToCenter | boolean | True if newly spawned particles will be oriented relative to the center of the emission area, false otherwise. |


ParticleSystem:setEmissionRate

Sets the amount of particles emitted per second.

ParticleSystem:setEmissionRate(rate)

| name | type | description |
| --- | --- | --- |
| rate | number | The amount of particles per second. |


ParticleSystem:setEmitterLifetime

Sets how long the particle system should emit particles (if -1 then it emits particles forever).

ParticleSystem:setEmitterLifetime(life)

| name | type | description |
| --- | --- | --- |
| life | number | The lifetime of the emitter (in seconds). |


ParticleSystem:setInsertMode

Sets the mode to use when the ParticleSystem adds new particles.

ParticleSystem:setInsertMode(mode)

| name | type | description |
| --- | --- | --- |
| mode | ParticleInsertMode | The mode to use when the ParticleSystem adds new particles. |


ParticleSystem:setLinearAcceleration

Sets the linear acceleration (acceleration along the x and y axes) for particles.

Every particle created will accelerate along the x and y axes between xmin,ymin and xmax,ymax.

ParticleSystem:setLinearAcceleration(xmin, ymin, xmax, ymax)

| name | type | description |
| --- | --- | --- |
| xmin | number | The minimum acceleration along the x axis. |
| ymin | number | The minimum acceleration along the y axis. |
| xmax | number | The maximum acceleration along the x axis. |
| ymax | number | The maximum acceleration along the y axis. |


ParticleSystem:setLinearDamping

Sets the amount of linear damping (constant deceleration) for particles.

ParticleSystem:setLinearDamping(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum amount of linear damping applied to particles. |
| max | number | The maximum amount of linear damping applied to particles. |


ParticleSystem:setOffset

Set the offset position which the particle sprite is rotated around.

If this function is not used, the particles rotate around their center.

ParticleSystem:setOffset(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x coordinate of the rotation offset. |
| y | number | The y coordinate of the rotation offset. |


ParticleSystem:setParticleLifetime

Sets the lifetime of the particles.

ParticleSystem:setParticleLifetime(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum life of the particles (in seconds). |
| max | number | The maximum life of the particles (in seconds). |


ParticleSystem:setPosition

Sets the position of the emitter.

ParticleSystem:setPosition(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | Position along x-axis. |
| y | number | Position along y-axis. |


ParticleSystem:setQuads

Sets a series of Quads to use for the particle sprites. Particles will choose a Quad from the list based on the particle's current lifetime, allowing for the use of animated sprite sheets with ParticleSystems.

ParticleSystem:setQuads(quad1, ...)

| name | type | description |
| --- | --- | --- |
| quad1 | Quad | The first Quad to use. |
| ... | Quad | Additional Quads to use. |

ParticleSystem:setQuads(quads)

| name | type | description |
| --- | --- | --- |
| quads | table | A table containing the Quads to use. |


ParticleSystem:setRadialAcceleration

Set the radial acceleration (away from the emitter).

ParticleSystem:setRadialAcceleration(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum acceleration. |
| max | number | The maximum acceleration. |


ParticleSystem:setRelativeRotation

Sets whether particle angles and rotations are relative to their velocities. If enabled, particles are aligned to the angle of their velocities and rotate relative to that angle.

ParticleSystem:setRelativeRotation(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable relative particle rotation, false to disable it. |


ParticleSystem:setRotation

Sets the rotation of the image upon particle creation (in radians).

ParticleSystem:setRotation(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum initial angle (radians). |
| max | number | The maximum initial angle (radians). |


ParticleSystem:setSizeVariation

Sets the amount of size variation (0 meaning no variation and 1 meaning full variation between start and end).

ParticleSystem:setSizeVariation(variation)

| name | type | description |
| --- | --- | --- |
| variation | number | The amount of variation (0 meaning no variation and 1 meaning full variation between start and end). |


ParticleSystem:setSizes

Sets a series of sizes by which to scale a particle sprite. 1.0 is normal size. The particle system will interpolate between each size evenly over the particle's lifetime.

At least one size must be specified. A maximum of eight may be used.

ParticleSystem:setSizes(size1, size2, size8)

| name | type | description |
| --- | --- | --- |
| size1 | number | The first size. |
| size2 | number | The second size. |
| size8 | number | The eighth size. |


ParticleSystem:setSpeed

Sets the speed of the particles.

ParticleSystem:setSpeed(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum linear speed of the particles. |
| max | number | The maximum linear speed of the particles. |


ParticleSystem:setSpin

Sets the spin of the sprite.

ParticleSystem:setSpin(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum spin (radians per second). |
| max | number | The maximum spin (radians per second). |


ParticleSystem:setSpinVariation

Sets the amount of spin variation (0 meaning no variation and 1 meaning full variation between start and end).

ParticleSystem:setSpinVariation(variation)

| name | type | description |
| --- | --- | --- |
| variation | number | The amount of variation (0 meaning no variation and 1 meaning full variation between start and end). |


ParticleSystem:setSpread

Sets the amount of spread for the system.

ParticleSystem:setSpread(spread)

| name | type | description |
| --- | --- | --- |
| spread | number | The amount of spread (radians). |


ParticleSystem:setTangentialAcceleration

Sets the tangential acceleration (acceleration perpendicular to the particle's direction).

ParticleSystem:setTangentialAcceleration(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum acceleration. |
| max | number | The maximum acceleration. |


ParticleSystem:setTexture

Sets the texture (Image or Canvas) to be used for the particles.

ParticleSystem:setTexture(texture)

| name | type | description |
| --- | --- | --- |
| texture | Texture | An Image or Canvas to use for the particles. |


ParticleSystem:start

Starts the particle emitter.

ParticleSystem:start()


ParticleSystem:stop

Stops the particle emitter, resetting the lifetime counter.

ParticleSystem:stop()


ParticleSystem:update

Updates the particle system; moving, creating and killing particles.

ParticleSystem:update(dt)

| name | type | description |
| --- | --- | --- |
| dt | number | The time (seconds) since last frame. |


PolygonShape:getPoints

Get the local coordinates of the polygon's vertices.

This function has a variable number of return values. It can be used in a nested fashion with love.graphics.polygon.

PolygonShape:getPoints()

| name | type | description |
| --- | --- | --- |
| x1 | number | The x-component of the first vertex. |
| y1 | number | The y-component of the first vertex. |
| x2 | number | The x-component of the second vertex. |
| y2 | number | The y-component of the second vertex. |


PrismaticJoint:areLimitsEnabled

Checks whether the limits are enabled.

PrismaticJoint:areLimitsEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false otherwise. |


PrismaticJoint:getAxis

Gets the world-space axis vector of the Prismatic Joint.

PrismaticJoint:getAxis()

| name | type | description |
| --- | --- | --- |
| x | number | The x-axis coordinate of the world-space axis vector. |
| y | number | The y-axis coordinate of the world-space axis vector. |


PrismaticJoint:getJointSpeed

Get the current joint angle speed.

PrismaticJoint:getJointSpeed()

| name | type | description |
| --- | --- | --- |
| s | number | Joint angle speed in meters/second. |


PrismaticJoint:getJointTranslation

Get the current joint translation.

PrismaticJoint:getJointTranslation()

| name | type | description |
| --- | --- | --- |
| t | number | Joint translation, usually in meters.. |


PrismaticJoint:getLimits

Gets the joint limits.

PrismaticJoint:getLimits()

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, usually in meters. |
| upper | number | The upper limit, usually in meters. |


PrismaticJoint:getLowerLimit

Gets the lower limit.

PrismaticJoint:getLowerLimit()

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, usually in meters. |


PrismaticJoint:getMaxMotorForce

Gets the maximum motor force.

PrismaticJoint:getMaxMotorForce()

| name | type | description |
| --- | --- | --- |
| f | number | The maximum motor force, usually in N. |


PrismaticJoint:getMotorForce

Returns the current motor force.

PrismaticJoint:getMotorForce(invdt)

| name | type | description |
| --- | --- | --- |
| invdt | number | How long the force applies. Usually the inverse time step or 1/dt. |

| name | type | description |
| --- | --- | --- |
| force | number | The force on the motor in newtons. |


PrismaticJoint:getMotorSpeed

Gets the motor speed.

PrismaticJoint:getMotorSpeed()

| name | type | description |
| --- | --- | --- |
| s | number | The motor speed, usually in meters per second. |


PrismaticJoint:getReferenceAngle

Gets the reference angle.

PrismaticJoint:getReferenceAngle()

| name | type | description |
| --- | --- | --- |
| angle | number | The reference angle in radians. |


PrismaticJoint:getUpperLimit

Gets the upper limit.

PrismaticJoint:getUpperLimit()

| name | type | description |
| --- | --- | --- |
| upper | number | The upper limit, usually in meters. |


PrismaticJoint:isMotorEnabled

Checks whether the motor is enabled.

PrismaticJoint:isMotorEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false if disabled. |


PrismaticJoint:setLimits

Sets the limits.

PrismaticJoint:setLimits(lower, upper)

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, usually in meters. |
| upper | number | The upper limit, usually in meters. |


PrismaticJoint:setLimitsEnabled

Enables/disables the joint limit.

PrismaticJoint:setLimitsEnabled()

| name | type | description |
| --- | --- | --- |
| enable | boolean | True if enabled, false if disabled. |


PrismaticJoint:setLowerLimit

Sets the lower limit.

PrismaticJoint:setLowerLimit(lower)

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, usually in meters. |


PrismaticJoint:setMaxMotorForce

Set the maximum motor force.

PrismaticJoint:setMaxMotorForce(f)

| name | type | description |
| --- | --- | --- |
| f | number | The maximum motor force, usually in N. |


PrismaticJoint:setMotorEnabled

Enables/disables the joint motor.

PrismaticJoint:setMotorEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable, false to disable. |


PrismaticJoint:setMotorSpeed

Sets the motor speed.

PrismaticJoint:setMotorSpeed(s)

| name | type | description |
| --- | --- | --- |
| s | number | The motor speed, usually in meters per second. |


PrismaticJoint:setUpperLimit

Sets the upper limit.

PrismaticJoint:setUpperLimit(upper)

| name | type | description |
| --- | --- | --- |
| upper | number | The upper limit, usually in meters. |


PulleyJoint:getConstant

Get the total length of the rope.

PulleyJoint:getConstant()

| name | type | description |
| --- | --- | --- |
| length | number | The length of the rope in the joint. |


PulleyJoint:getGroundAnchors

Get the ground anchor positions in world coordinates.

PulleyJoint:getGroundAnchors()

| name | type | description |
| --- | --- | --- |
| a1x | number | The x coordinate of the first anchor. |
| a1y | number | The y coordinate of the first anchor. |
| a2x | number | The x coordinate of the second anchor. |
| a2y | number | The y coordinate of the second anchor. |


PulleyJoint:getLengthA

Get the current length of the rope segment attached to the first body.

PulleyJoint:getLengthA()

| name | type | description |
| --- | --- | --- |
| length | number | The length of the rope segment. |


PulleyJoint:getLengthB

Get the current length of the rope segment attached to the second body.

PulleyJoint:getLengthB()

| name | type | description |
| --- | --- | --- |
| length | number | The length of the rope segment. |


PulleyJoint:getMaxLengths

Get the maximum lengths of the rope segments.

PulleyJoint:getMaxLengths()

| name | type | description |
| --- | --- | --- |
| len1 | number | The maximum length of the first rope segment. |
| len2 | number | The maximum length of the second rope segment. |


PulleyJoint:getRatio

Get the pulley ratio.

PulleyJoint:getRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The pulley ratio of the joint. |


PulleyJoint:setConstant

Set the total length of the rope.

Setting a new length for the rope updates the maximum length values of the joint.

PulleyJoint:setConstant(length)

| name | type | description |
| --- | --- | --- |
| length | number | The new length of the rope in the joint. |


PulleyJoint:setMaxLengths

Set the maximum lengths of the rope segments.

The physics module also imposes maximum values for the rope segments. If the parameters exceed these values, the maximum values are set instead of the requested values.

PulleyJoint:setMaxLengths(max1, max2)

| name | type | description |
| --- | --- | --- |
| max1 | number | The new maximum length of the first segment. |
| max2 | number | The new maximum length of the second segment. |


PulleyJoint:setRatio

Set the pulley ratio.

PulleyJoint:setRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The new pulley ratio of the joint. |


Quad:getTextureDimensions

Gets reference texture dimensions initially specified in love.graphics.newQuad.

Quad:getTextureDimensions()

| name | type | description |
| --- | --- | --- |
| sw | number | The Texture width used by the Quad. |
| sh | number | The Texture height used by the Quad. |


Quad:getViewport

Gets the current viewport of this Quad.

Quad:getViewport()

| name | type | description |
| --- | --- | --- |
| x | number | The top-left corner along the x-axis. |
| y | number | The top-left corner along the y-axis. |
| w | number | The width of the viewport. |
| h | number | The height of the viewport. |


Quad:setViewport

Sets the texture coordinates according to a viewport.

Quad:setViewport(x, y, w, h, sw, sh)

| name | type | description |
| --- | --- | --- |
| x | number | The top-left corner along the x-axis. |
| y | number | The top-left corner along the y-axis. |
| w | number | The width of the viewport. |
| h | number | The height of the viewport. |
| sw | number | Optional new reference width, the width of the Texture. Must be greater than 0 if set. |
| sh | number | Optional new reference height, the height of the Texture. Must be greater than 0 if set. |


RandomGenerator:getSeed

Gets the seed of the random number generator object.

The seed is split into two numbers due to Lua's use of doubles for all number values - doubles can't accurately represent integer  values above 2^53, but the seed value is an integer number in the range of 2^64 - 1.

RandomGenerator:getSeed()

| name | type | description |
| --- | --- | --- |
| low | number | Integer number representing the lower 32 bits of the RandomGenerator's 64 bit seed value. |
| high | number | Integer number representing the higher 32 bits of the RandomGenerator's 64 bit seed value. |


RandomGenerator:getState

Gets the current state of the random number generator. This returns an opaque string which is only useful for later use with RandomGenerator:setState in the same major version of LÖVE.

This is different from RandomGenerator:getSeed in that getState gets the RandomGenerator's current state, whereas getSeed gets the previously set seed number.

RandomGenerator:getState()

| name | type | description |
| --- | --- | --- |
| state | string | The current state of the RandomGenerator object, represented as a string. |


RandomGenerator:random

Generates a pseudo-random number in a platform independent manner.

RandomGenerator:random()

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random number. |

RandomGenerator:random(max)

| name | type | description |
| --- | --- | --- |
| max | number | The maximum possible value it should return. |

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random integer number. |

RandomGenerator:random(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum possible value it should return. |
| max | number | The maximum possible value it should return. |

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random integer number. |


RandomGenerator:randomNormal

Get a normally distributed pseudo random number.

RandomGenerator:randomNormal(stddev, mean)

| name | type | description |
| --- | --- | --- |
| stddev | number | Standard deviation of the distribution. |
| mean | number | The mean of the distribution. |

| name | type | description |
| --- | --- | --- |
| number | number | Normally distributed random number with variance (stddev)² and the specified mean. |


RandomGenerator:setSeed

Sets the seed of the random number generator using the specified integer number.

RandomGenerator:setSeed(seed)

| name | type | description |
| --- | --- | --- |
| seed | number | The integer number with which you want to seed the randomization. Must be within the range of 2^53. |

RandomGenerator:setSeed(low, high)

| name | type | description |
| --- | --- | --- |
| low | number | The lower 32 bits of the seed value. Must be within the range of 2^32 - 1. |
| high | number | The higher 32 bits of the seed value. Must be within the range of 2^32 - 1. |


RandomGenerator:setState

Sets the current state of the random number generator. The value used as an argument for this function is an opaque string and should only originate from a previous call to RandomGenerator:getState in the same major version of LÖVE.

This is different from RandomGenerator:setSeed in that setState directly sets the RandomGenerator's current implementation-dependent state, whereas setSeed gives it a new seed value.

RandomGenerator:setState(state)

| name | type | description |
| --- | --- | --- |
| state | string | The new state of the RandomGenerator object, represented as a string. This should originate from a previous call to RandomGenerator:getState. |


Rasterizer:getAdvance

Gets font advance.

Rasterizer:getAdvance()

| name | type | description |
| --- | --- | --- |
| advance | number | Font advance. |


Rasterizer:getAscent

Gets ascent height.

Rasterizer:getAscent()

| name | type | description |
| --- | --- | --- |
| height | number | Ascent height. |


Rasterizer:getDescent

Gets descent height.

Rasterizer:getDescent()

| name | type | description |
| --- | --- | --- |
| height | number | Descent height. |


Rasterizer:getGlyphCount

Gets number of glyphs in font.

Rasterizer:getGlyphCount()

| name | type | description |
| --- | --- | --- |
| count | number | Glyphs count. |


Rasterizer:getGlyphData

Gets glyph data of a specified glyph.

Rasterizer:getGlyphData(glyph)

| name | type | description |
| --- | --- | --- |
| glyph | string | Glyph |

| name | type | description |
| --- | --- | --- |
| glyphData | GlyphData | Glyph data |

Rasterizer:getGlyphData(glyphNumber)

| name | type | description |
| --- | --- | --- |
| glyphNumber | number | Glyph number |

| name | type | description |
| --- | --- | --- |
| glyphData | GlyphData | Glyph data |


Rasterizer:getHeight

Gets font height.

Rasterizer:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | Font height |


Rasterizer:getLineHeight

Gets line height of a font.

Rasterizer:getLineHeight()

| name | type | description |
| --- | --- | --- |
| height | number | Line height of a font. |


Rasterizer:hasGlyphs

Checks if font contains specified glyphs.

Rasterizer:hasGlyphs(glyph1, ...)

| name | type | description |
| --- | --- | --- |
| glyph1 | string or number | Glyph |
| ... | string or number | Additional glyphs |

| name | type | description |
| --- | --- | --- |
| hasGlyphs | boolean | Whatever font contains specified glyphs. |


RecordingDevice:getBitDepth

Gets the number of bits per sample in the data currently being recorded.

RecordingDevice:getBitDepth()

| name | type | description |
| --- | --- | --- |
| bits | number | The number of bits per sample in the data that's currently being recorded. |


RecordingDevice:getChannelCount

Gets the number of channels currently being recorded (mono or stereo).

RecordingDevice:getChannelCount()

| name | type | description |
| --- | --- | --- |
| channels | number | The number of channels being recorded (1 for mono, 2 for stereo). |


RecordingDevice:getData

Gets all recorded audio SoundData stored in the device's internal ring buffer.

The internal ring buffer is cleared when this function is called, so calling it again will only get audio recorded after the previous call. If the device's internal ring buffer completely fills up before getData is called, the oldest data that doesn't fit into the buffer will be lost.

RecordingDevice:getData()

| name | type | description |
| --- | --- | --- |
| data | SoundData | The recorded audio data, or nil if the device isn't recording. |


RecordingDevice:getName

Gets the name of the recording device.

RecordingDevice:getName()

| name | type | description |
| --- | --- | --- |
| name | string | The name of the device. |


RecordingDevice:getSampleCount

Gets the number of currently recorded samples.

RecordingDevice:getSampleCount()

| name | type | description |
| --- | --- | --- |
| samples | number | The number of samples that have been recorded so far. |


RecordingDevice:getSampleRate

Gets the number of samples per second currently being recorded.

RecordingDevice:getSampleRate()

| name | type | description |
| --- | --- | --- |
| rate | number | The number of samples being recorded per second (sample rate). |


RecordingDevice:isRecording

Gets whether the device is currently recording.

RecordingDevice:isRecording()

| name | type | description |
| --- | --- | --- |
| recording | boolean | True if the recording, false otherwise. |


RecordingDevice:start

Begins recording audio using this device.

RecordingDevice:start(samplecount, samplerate, bitdepth, channels)

| name | type | description |
| --- | --- | --- |
| samplecount | number | The maximum number of samples to store in an internal ring buffer when recording. RecordingDevice:getData clears the internal buffer when called. |
| samplerate | number | The number of samples per second to store when recording. |
| bitdepth | number | The number of bits per sample. |
| channels | number | Whether to record in mono or stereo. Most microphones don't support more than 1 channel. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the device successfully began recording using the specified parameters, false if not. |


RecordingDevice:stop

Stops recording audio from this device. Any sound data currently in the device's buffer will be returned.

RecordingDevice:stop()

| name | type | description |
| --- | --- | --- |
| data | SoundData | The sound data currently in the device's buffer, or nil if the device wasn't recording. |


RevoluteJoint:areLimitsEnabled

Checks whether limits are enabled.

RevoluteJoint:areLimitsEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false otherwise. |


RevoluteJoint:getJointAngle

Get the current joint angle.

RevoluteJoint:getJointAngle()

| name | type | description |
| --- | --- | --- |
| angle | number | The joint angle in radians. |


RevoluteJoint:getJointSpeed

Get the current joint angle speed.

RevoluteJoint:getJointSpeed()

| name | type | description |
| --- | --- | --- |
| s | number | Joint angle speed in radians/second. |


RevoluteJoint:getLimits

Gets the joint limits.

RevoluteJoint:getLimits()

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, in radians. |
| upper | number | The upper limit, in radians. |


RevoluteJoint:getLowerLimit

Gets the lower limit.

RevoluteJoint:getLowerLimit()

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, in radians. |


RevoluteJoint:getMaxMotorTorque

Gets the maximum motor force.

RevoluteJoint:getMaxMotorTorque()

| name | type | description |
| --- | --- | --- |
| f | number | The maximum motor force, in Nm. |


RevoluteJoint:getMotorSpeed

Gets the motor speed.

RevoluteJoint:getMotorSpeed()

| name | type | description |
| --- | --- | --- |
| s | number | The motor speed, radians per second. |


RevoluteJoint:getMotorTorque

Get the current motor force.

RevoluteJoint:getMotorTorque()

| name | type | description |
| --- | --- | --- |
| f | number | The current motor force, in Nm. |


RevoluteJoint:getReferenceAngle

Gets the reference angle.

RevoluteJoint:getReferenceAngle()

| name | type | description |
| --- | --- | --- |
| angle | number | The reference angle in radians. |


RevoluteJoint:getUpperLimit

Gets the upper limit.

RevoluteJoint:getUpperLimit()

| name | type | description |
| --- | --- | --- |
| upper | number | The upper limit, in radians. |


RevoluteJoint:hasLimitsEnabled

Checks whether limits are enabled.

RevoluteJoint:hasLimitsEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false otherwise. |


RevoluteJoint:isMotorEnabled

Checks whether the motor is enabled.

RevoluteJoint:isMotorEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if enabled, false if disabled. |


RevoluteJoint:setLimits

Sets the limits.

RevoluteJoint:setLimits(lower, upper)

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, in radians. |
| upper | number | The upper limit, in radians. |


RevoluteJoint:setLimitsEnabled

Enables/disables the joint limit.

RevoluteJoint:setLimitsEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable, false to disable. |


RevoluteJoint:setLowerLimit

Sets the lower limit.

RevoluteJoint:setLowerLimit(lower)

| name | type | description |
| --- | --- | --- |
| lower | number | The lower limit, in radians. |


RevoluteJoint:setMaxMotorTorque

Set the maximum motor force.

RevoluteJoint:setMaxMotorTorque(f)

| name | type | description |
| --- | --- | --- |
| f | number | The maximum motor force, in Nm. |


RevoluteJoint:setMotorEnabled

Enables/disables the joint motor.

RevoluteJoint:setMotorEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable, false to disable. |


RevoluteJoint:setMotorSpeed

Sets the motor speed.

RevoluteJoint:setMotorSpeed(s)

| name | type | description |
| --- | --- | --- |
| s | number | The motor speed, radians per second. |


RevoluteJoint:setUpperLimit

Sets the upper limit.

RevoluteJoint:setUpperLimit(upper)

| name | type | description |
| --- | --- | --- |
| upper | number | The upper limit, in radians. |


RopeJoint:getMaxLength

Gets the maximum length of a RopeJoint.

RopeJoint:getMaxLength()

| name | type | description |
| --- | --- | --- |
| maxLength | number | The maximum length of the RopeJoint. |


RopeJoint:setMaxLength

Sets the maximum length of a RopeJoint.

RopeJoint:setMaxLength(maxLength)

| name | type | description |
| --- | --- | --- |
| maxLength | number | The new maximum length of the RopeJoint. |


Shader:getWarnings

Returns any warning and error messages from compiling the shader code. This can be used for debugging your shaders if there's anything the graphics hardware doesn't like.

Shader:getWarnings()

| name | type | description |
| --- | --- | --- |
| warnings | string | Warning and error messages (if any). |


Shader:hasUniform

Gets whether a uniform / extern variable exists in the Shader.

If a graphics driver's shader compiler determines that a uniform / extern variable doesn't affect the final output of the shader, it may optimize the variable out. This function will return false in that case.

Shader:hasUniform(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the uniform variable. |

| name | type | description |
| --- | --- | --- |
| hasuniform | boolean | Whether the uniform exists in the shader and affects its final output. |


Shader:send

Sends one or more values to a special (''uniform'') variable inside the shader. Uniform variables have to be marked using the ''uniform'' or ''extern'' keyword, e.g.

uniform float time;  // 'float' is the typical number type used in GLSL shaders.

uniform float varsvec2 light_pos;

uniform vec4 colors[4;

The corresponding send calls would be

shader:send('time', t)

shader:send('vars',a,b)

shader:send('light_pos', {light_x, light_y})

shader:send('colors', {r1, g1, b1, a1},  {r2, g2, b2, a2},  {r3, g3, b3, a3},  {r4, g4, b4, a4})

Uniform / extern variables are read-only in the shader code and remain constant until modified by a Shader:send call. Uniform variables can be accessed in both the Vertex and Pixel components of a shader, as long as the variable is declared in each.

Shader:send(name, number, ...)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the number to send to the shader. |
| number | number | Number to send to store in the uniform variable. |
| ... | number | Additional numbers to send if the uniform variable is an array. |

Shader:send(name, vector, ...)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the vector to send to the shader. |
| vector | table | Numbers to send to the uniform variable as a vector. The number of elements in the table determines the type of the vector (e.g. two numbers -&gt; vec2). At least two and at most four numbers can be used. |
| ... | table | Additional vectors to send if the uniform variable is an array. All vectors need to be of the same size (e.g. only vec3's). |

Shader:send(name, matrix, ...)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the matrix to send to the shader. |
| matrix | table | 2x2, 3x3, or 4x4 matrix to send to the uniform variable. Using table form: {{a,b,c,d}, {e,f,g,h}, ... } or (since version 0.10.2) {a,b,c,d, e,f,g,h, ...}. The order in 0.10.2 is column-major; starting in 11.0 it's row-major instead. |
| ... | table | Additional matrices of the same type as ''matrix'' to store in a uniform array. |

Shader:send(name, texture)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the Texture to send to the shader. |
| texture | Texture | Texture (Image or Canvas) to send to the uniform variable. |

Shader:send(name, boolean, ...)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the boolean to send to the shader. |
| boolean | boolean | Boolean to send to store in the uniform variable. |
| ... | boolean | Additional booleans to send if the uniform variable is an array. |

Shader:send(name, matrixlayout, matrix, ...)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the matrix to send to the shader. |
| matrixlayout | MatrixLayout | The layout (row- or column-major) of the matrix. |
| matrix | table | 2x2, 3x3, or 4x4 matrix to send to the uniform variable. Using table form: {{a,b,c,d}, {e,f,g,h}, ... } or {a,b,c,d, e,f,g,h, ...}. |
| ... | table | Additional matrices of the same type as ''matrix'' to store in a uniform array. |

Shader:send(name, data, offset, size)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the uniform to send to the shader. |
| data | Data | Data object containing the values to send. |
| offset | number | Offset in bytes from the start of the Data object. |
| size | number | Size in bytes of the data to send. If nil, as many bytes as the specified uniform uses will be copied. |

Shader:send(name, data, matrixlayout, offset, size)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the uniform matrix to send to the shader. |
| data | Data | Data object containing the values to send. |
| matrixlayout | MatrixLayout | The layout (row- or column-major) of the matrix in memory. |
| offset | number | Offset in bytes from the start of the Data object. |
| size | number | Size in bytes of the data to send. If nil, as many bytes as the specified uniform uses will be copied. |

Shader:send(name, matrixlayout, data, offset, size)

| name | type | description |
| --- | --- | --- |
| name | string | Name of the uniform matrix to send to the shader. |
| matrixlayout | MatrixLayout | The layout (row- or column-major) of the matrix in memory. |
| data | Data | Data object containing the values to send. |
| offset | number | Offset in bytes from the start of the Data object. |
| size | number | Size in bytes of the data to send. If nil, as many bytes as the specified uniform uses will be copied. |


Shader:sendColor

Sends one or more colors to a special (''extern'' / ''uniform'') vec3 or vec4 variable inside the shader. The color components must be in the range of 1. The colors are gamma-corrected if global gamma-correction is enabled.

Extern variables must be marked using the ''extern'' keyword, e.g.

extern vec4 Color;

The corresponding sendColor call would be

shader:sendColor('Color', {r, g, b, a})

Extern variables can be accessed in both the Vertex and Pixel stages of a shader, as long as the variable is declared in each.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

Shader:sendColor(name, color, ...)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the color extern variable to send to in the shader. |
| color | table | A table with red, green, blue, and optional alpha color components in the range of 1 to send to the extern as a vector. |
| ... | table | Additional colors to send in case the extern is an array. All colors need to be of the same size (e.g. only vec3's). |


Shape:computeAABB

Returns the points of the bounding box for the transformed shape.

Shape:computeAABB(tx, ty, tr, childIndex)

| name | type | description |
| --- | --- | --- |
| tx | number | The translation of the shape on the x-axis. |
| ty | number | The translation of the shape on the y-axis. |
| tr | number | The shape rotation. |
| childIndex | number | The index of the child to compute the bounding box of. |

| name | type | description |
| --- | --- | --- |
| topLeftX | number | The x position of the top-left point. |
| topLeftY | number | The y position of the top-left point. |
| bottomRightX | number | The x position of the bottom-right point. |
| bottomRightY | number | The y position of the bottom-right point. |


Shape:computeMass

Computes the mass properties for the shape with the specified density.

Shape:computeMass(density)

| name | type | description |
| --- | --- | --- |
| density | number | The shape density. |

| name | type | description |
| --- | --- | --- |
| x | number | The x postition of the center of mass. |
| y | number | The y postition of the center of mass. |
| mass | number | The mass of the shape. |
| inertia | number | The rotational inertia. |


Shape:getChildCount

Returns the number of children the shape has.

Shape:getChildCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of children. |


Shape:getRadius

Gets the radius of the shape.

Shape:getRadius()

| name | type | description |
| --- | --- | --- |
| radius | number | The radius of the shape. |


Shape:getType

Gets a string representing the Shape.

This function can be useful for conditional debug drawing.

Shape:getType()

| name | type | description |
| --- | --- | --- |
| type | ShapeType | The type of the Shape. |


Shape:rayCast

Casts a ray against the shape and returns the surface normal vector and the line position where the ray hit. If the ray missed the shape, nil will be returned. The Shape can be transformed to get it into the desired position.

The ray starts on the first point of the input line and goes towards the second point of the line. The fourth argument is the maximum distance the ray is going to travel as a scale factor of the input line length.

The childIndex parameter is used to specify which child of a parent shape, such as a ChainShape, will be ray casted. For ChainShapes, the index of 1 is the first edge on the chain. Ray casting a parent shape will only test the child specified so if you want to test every shape of the parent, you must loop through all of its children.

The world position of the impact can be calculated by multiplying the line vector with the third return value and adding it to the line starting point.

hitx, hity = x1 + (x2 - x1) * fraction, y1 + (y2 - y1) * fraction

Shape:rayCast(x1, y1, x2, y2, maxFraction, tx, ty, tr, childIndex)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the input line starting point. |
| y1 | number | The y position of the input line starting point. |
| x2 | number | The x position of the input line end point. |
| y2 | number | The y position of the input line end point. |
| maxFraction | number | Ray length parameter. |
| tx | number | The translation of the shape on the x-axis. |
| ty | number | The translation of the shape on the y-axis. |
| tr | number | The shape rotation. |
| childIndex | number | The index of the child the ray gets cast against. |

| name | type | description |
| --- | --- | --- |
| xn | number | The x component of the normal vector of the edge where the ray hit the shape. |
| yn | number | The y component of the normal vector of the edge where the ray hit the shape. |
| fraction | number | The position on the input line where the intersection happened as a factor of the line length. |


Shape:testPoint

This is particularly useful for mouse interaction with the shapes. By looping through all shapes and testing the mouse position with this function, we can find which shapes the mouse touches.

Shape:testPoint(tx, ty, tr, x, y)

| name | type | description |
| --- | --- | --- |
| tx | number | Translates the shape along the x-axis. |
| ty | number | Translates the shape along the y-axis. |
| tr | number | Rotates the shape. |
| x | number | The x-component of the point. |
| y | number | The y-component of the point. |

| name | type | description |
| --- | --- | --- |
| hit | boolean | True if inside, false if outside |


SoundData:getBitDepth

Returns the number of bits per sample.

SoundData:getBitDepth()

| name | type | description |
| --- | --- | --- |
| bitdepth | number | Either 8, or 16. |


SoundData:getChannelCount

Returns the number of channels in the SoundData.

SoundData:getChannelCount()

| name | type | description |
| --- | --- | --- |
| channels | number | 1 for mono, 2 for stereo. |


SoundData:getDuration

Gets the duration of the sound data.

SoundData:getDuration()

| name | type | description |
| --- | --- | --- |
| duration | number | The duration of the sound data in seconds. |


SoundData:getSample

Gets the value of the sample-point at the specified position. For stereo SoundData objects, the data from the left and right channels are interleaved in that order.

SoundData:getSample(i)

| name | type | description |
| --- | --- | --- |
| i | number | An integer value specifying the position of the sample (starting at 0). |

| name | type | description |
| --- | --- | --- |
| sample | number | The normalized samplepoint (range -1.0 to 1.0). |

SoundData:getSample(i, channel)

| name | type | description |
| --- | --- | --- |
| i | number | An integer value specifying the position of the sample (starting at 0). |
| channel | number | The index of the channel to get within the given sample. |

| name | type | description |
| --- | --- | --- |
| sample | number | The normalized samplepoint (range -1.0 to 1.0). |


SoundData:getSampleCount

Returns the number of samples per channel of the SoundData.

SoundData:getSampleCount()

| name | type | description |
| --- | --- | --- |
| count | number | Total number of samples. |


SoundData:getSampleRate

Returns the sample rate of the SoundData.

SoundData:getSampleRate()

| name | type | description |
| --- | --- | --- |
| rate | number | Number of samples per second. |


SoundData:setSample

Sets the value of the sample-point at the specified position. For stereo SoundData objects, the data from the left and right channels are interleaved in that order.

SoundData:setSample(i, sample)

| name | type | description |
| --- | --- | --- |
| i | number | An integer value specifying the position of the sample (starting at 0). |
| sample | number | The normalized samplepoint (range -1.0 to 1.0). |

SoundData:setSample(i, channel, sample)

| name | type | description |
| --- | --- | --- |
| i | number | An integer value specifying the position of the sample (starting at 0). |
| channel | number | The index of the channel to set within the given sample. |
| sample | number | The normalized samplepoint (range -1.0 to 1.0). |


Source:clone

Creates an identical copy of the Source in the stopped state.

Static Sources will use significantly less memory and take much less time to be created if Source:clone is used to create them instead of love.audio.newSource, so this method should be preferred when making multiple Sources which play the same sound.

Source:clone()

| name | type | description |
| --- | --- | --- |
| source | Source | The new identical copy of this Source. |


Source:getActiveEffects

Gets a list of the Source's active effect names.

Source:getActiveEffects()

| name | type | description |
| --- | --- | --- |
| effects | table | A list of the source's active effect names. |


Source:getAirAbsorption

Gets the amount of air absorption applied to the Source.

By default the value is set to 0 which means that air absorption effects are disabled. A value of 1 will apply high frequency attenuation to the Source at a rate of 0.05 dB per meter.

Source:getAirAbsorption()

| name | type | description |
| --- | --- | --- |
| amount | number | The amount of air absorption applied to the Source. |


Source:getAttenuationDistances

Gets the reference and maximum attenuation distances of the Source. The values, combined with the current DistanceModel, affect how the Source's volume attenuates based on distance from the listener.

Source:getAttenuationDistances()

| name | type | description |
| --- | --- | --- |
| ref | number | The current reference attenuation distance. If the current DistanceModel is clamped, this is the minimum distance before the Source is no longer attenuated. |
| max | number | The current maximum attenuation distance. |


Source:getChannelCount

Gets the number of channels in the Source. Only 1-channel (mono) Sources can use directional and positional effects.

Source:getChannelCount()

| name | type | description |
| --- | --- | --- |
| channels | number | 1 for mono, 2 for stereo. |


Source:getCone

Gets the Source's directional volume cones. Together with Source:setDirection, the cone angles allow for the Source's volume to vary depending on its direction.

Source:getCone()

| name | type | description |
| --- | --- | --- |
| innerAngle | number | The inner angle from the Source's direction, in radians. The Source will play at normal volume if the listener is inside the cone defined by this angle. |
| outerAngle | number | The outer angle from the Source's direction, in radians. The Source will play at a volume between the normal and outer volumes, if the listener is in between the cones defined by the inner and outer angles. |
| outerVolume | number | The Source's volume when the listener is outside both the inner and outer cone angles. |


Source:getDirection

Gets the direction of the Source.

Source:getDirection()

| name | type | description |
| --- | --- | --- |
| x | number | The X part of the direction vector. |
| y | number | The Y part of the direction vector. |
| z | number | The Z part of the direction vector. |


Source:getDuration

Gets the duration of the Source. For streaming Sources it may not always be sample-accurate, and may return -1 if the duration cannot be determined at all.

Source:getDuration(unit)

| name | type | description |
| --- | --- | --- |
| unit | TimeUnit | The time unit for the return value. |

| name | type | description |
| --- | --- | --- |
| duration | number | The duration of the Source, or -1 if it cannot be determined. |


Source:getEffect

Gets the filter settings associated to a specific effect.

This function returns nil if the effect was applied with no filter settings associated to it.

Source:getEffect(name, filtersettings)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect. |
| filtersettings | table | An optional empty table that will be filled with the filter settings. |

| name | type | description |
| --- | --- | --- |
| filtersettings | table | The settings for the filter associated to this effect, or nil if the effect is not present in this Source or has no filter associated. The table has the following fields: |


Source:getFilter

Gets the filter settings currently applied to the Source.

Source:getFilter()

| name | type | description |
| --- | --- | --- |
| settings | table | The filter settings to use for this Source, or nil if the Source has no active filter. The table has the following fields: |


Source:getFreeBufferCount

Gets the number of free buffer slots in a queueable Source. If the queueable Source is playing, this value will increase up to the amount the Source was created with. If the queueable Source is stopped, it will process all of its internal buffers first, in which case this function will always return the amount it was created with.

Source:getFreeBufferCount()

| name | type | description |
| --- | --- | --- |
| buffers | number | How many more SoundData objects can be queued up. |


Source:getPitch

Gets the current pitch of the Source.

Source:getPitch()

| name | type | description |
| --- | --- | --- |
| pitch | number | The pitch, where 1.0 is normal. |


Source:getPosition

Gets the position of the Source.

Source:getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | The X position of the Source. |
| y | number | The Y position of the Source. |
| z | number | The Z position of the Source. |


Source:getRolloff

Returns the rolloff factor of the source.

Source:getRolloff()

| name | type | description |
| --- | --- | --- |
| rolloff | number | The rolloff factor. |


Source:getType

Gets the type of the Source.

Source:getType()

| name | type | description |
| --- | --- | --- |
| sourcetype | SourceType | The type of the source. |


Source:getVelocity

Gets the velocity of the Source.

Source:getVelocity()

| name | type | description |
| --- | --- | --- |
| x | number | The X part of the velocity vector. |
| y | number | The Y part of the velocity vector. |
| z | number | The Z part of the velocity vector. |


Source:getVolume

Gets the current volume of the Source.

Source:getVolume()

| name | type | description |
| --- | --- | --- |
| volume | number | The volume of the Source, where 1.0 is normal volume. |


Source:getVolumeLimits

Returns the volume limits of the source.

Source:getVolumeLimits()

| name | type | description |
| --- | --- | --- |
| min | number | The minimum volume. |
| max | number | The maximum volume. |


Source:isLooping

Returns whether the Source will loop.

Source:isLooping()

| name | type | description |
| --- | --- | --- |
| loop | boolean | True if the Source will loop, false otherwise. |


Source:isPlaying

Returns whether the Source is playing.

Source:isPlaying()

| name | type | description |
| --- | --- | --- |
| playing | boolean | True if the Source is playing, false otherwise. |


Source:isRelative

Gets whether the Source's position, velocity, direction, and cone angles are relative to the listener.

Source:isRelative()

| name | type | description |
| --- | --- | --- |
| relative | boolean | True if the position, velocity, direction and cone angles are relative to the listener, false if they're absolute. |


Source:pause

Pauses the Source.

Source:pause()


Source:play

Starts playing the Source.

Source:play()

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the Source was able to successfully start playing. |


Source:queue

Queues SoundData for playback in a queueable Source.

This method requires the Source to be created via love.audio.newQueueableSource.

Source:queue(sounddata)

| name | type | description |
| --- | --- | --- |
| sounddata | SoundData | The data to queue. The SoundData's sample rate, bit depth, and channel count must match the Source's. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the data was successfully queued for playback, false if there were no available buffers to use for queueing. |


Source:seek

Sets the currently playing position of the Source.

Source:seek(offset, unit)

| name | type | description |
| --- | --- | --- |
| offset | number | The position to seek to. |
| unit | TimeUnit | The unit of the position value. |


Source:setAirAbsorption

Sets the amount of air absorption applied to the Source.

By default the value is set to 0 which means that air absorption effects are disabled. A value of 1 will apply high frequency attenuation to the Source at a rate of 0.05 dB per meter.

Air absorption can simulate sound transmission through foggy air, dry air, smoky atmosphere, etc. It can be used to simulate different atmospheric conditions within different locations in an area.

Source:setAirAbsorption(amount)

| name | type | description |
| --- | --- | --- |
| amount | number | The amount of air absorption applied to the Source. Must be between 0 and 10. |


Source:setAttenuationDistances

Sets the reference and maximum attenuation distances of the Source. The parameters, combined with the current DistanceModel, affect how the Source's volume attenuates based on distance.

Distance attenuation is only applicable to Sources based on mono (rather than stereo) audio.

Source:setAttenuationDistances(ref, max)

| name | type | description |
| --- | --- | --- |
| ref | number | The new reference attenuation distance. If the current DistanceModel is clamped, this is the minimum attenuation distance. |
| max | number | The new maximum attenuation distance. |


Source:setCone

Sets the Source's directional volume cones. Together with Source:setDirection, the cone angles allow for the Source's volume to vary depending on its direction.

Source:setCone(innerAngle, outerAngle, outerVolume)

| name | type | description |
| --- | --- | --- |
| innerAngle | number | The inner angle from the Source's direction, in radians. The Source will play at normal volume if the listener is inside the cone defined by this angle. |
| outerAngle | number | The outer angle from the Source's direction, in radians. The Source will play at a volume between the normal and outer volumes, if the listener is in between the cones defined by the inner and outer angles. |
| outerVolume | number | The Source's volume when the listener is outside both the inner and outer cone angles. |


Source:setDirection

Sets the direction vector of the Source. A zero vector makes the source non-directional.

Source:setDirection(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The X part of the direction vector. |
| y | number | The Y part of the direction vector. |
| z | number | The Z part of the direction vector. |


Source:setEffect

Applies an audio effect to the Source.

The effect must have been previously defined using love.audio.setEffect.

Source:setEffect(name, enable)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect previously set up with love.audio.setEffect. |
| enable | boolean | If false and the given effect name was previously enabled on this Source, disables the effect. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the effect was successfully applied to this Source. |

Source:setEffect(name, filtersettings)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect previously set up with love.audio.setEffect. |
| filtersettings | table | The filter settings to apply prior to the effect, with the following fields: |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the effect and filter were successfully applied to this Source. |


Source:setFilter

Sets a low-pass, high-pass, or band-pass filter to apply when playing the Source.

Source:setFilter(settings)

| name | type | description |
| --- | --- | --- |
| settings | table | The filter settings to use for this Source, with the following fields: |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the filter was successfully applied to the Source. |

Source:setFilter()


Source:setLooping

Sets whether the Source should loop.

Source:setLooping(loop)

| name | type | description |
| --- | --- | --- |
| loop | boolean | True if the source should loop, false otherwise. |


Source:setPitch

Sets the pitch of the Source.

Source:setPitch(pitch)

| name | type | description |
| --- | --- | --- |
| pitch | number | Calculated with regard to 1 being the base pitch. Each reduction by 50 percent equals a pitch shift of -12 semitones (one octave reduction). Each doubling equals a pitch shift of 12 semitones (one octave increase). Zero is not a legal value. |


Source:setPosition

Sets the position of the Source. Please note that this only works for mono (i.e. non-stereo) sound files!

Source:setPosition(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The X position of the Source. |
| y | number | The Y position of the Source. |
| z | number | The Z position of the Source. |


Source:setRelative

Sets whether the Source's position, velocity, direction, and cone angles are relative to the listener, or absolute.

By default, all sources are absolute and therefore relative to the origin of love's coordinate system 0, 0. Only absolute sources are affected by the position of the listener. Please note that positional audio only works for mono (i.e. non-stereo) sources.

Source:setRelative(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to make the position, velocity, direction and cone angles relative to the listener, false to make them absolute. |


Source:setRolloff

Sets the rolloff factor which affects the strength of the used distance attenuation.

Extended information and detailed formulas can be found in the chapter '3.4. Attenuation By Distance' of OpenAL 1.1 specification.

Source:setRolloff(rolloff)

| name | type | description |
| --- | --- | --- |
| rolloff | number | The new rolloff factor. |


Source:setVelocity

Sets the velocity of the Source.

This does '''not''' change the position of the Source, but lets the application know how it has to calculate the doppler effect.

Source:setVelocity(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The X part of the velocity vector. |
| y | number | The Y part of the velocity vector. |
| z | number | The Z part of the velocity vector. |


Source:setVolume

Sets the current volume of the Source.

Source:setVolume(volume)

| name | type | description |
| --- | --- | --- |
| volume | number | The volume for a Source, where 1.0 is normal volume. Volume cannot be raised above 1.0. |


Source:setVolumeLimits

Sets the volume limits of the source. The limits have to be numbers from 0 to 1.

Source:setVolumeLimits(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum volume. |
| max | number | The maximum volume. |


Source:stop

Stops a Source.

Source:stop()


Source:tell

Gets the currently playing position of the Source.

Source:tell(unit)

| name | type | description |
| --- | --- | --- |
| unit | TimeUnit | The type of unit for the return value. |

| name | type | description |
| --- | --- | --- |
| position | number | The currently playing position of the Source. |


SpriteBatch:add

Adds a sprite to the batch. Sprites are drawn in the order they are added.

SpriteBatch:add(x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shear factor (x-axis). |
| ky | number | Shear factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| id | number | An identifier for the added sprite. |

SpriteBatch:add(quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| quad | Quad | The Quad to add. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shear factor (x-axis). |
| ky | number | Shear factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| id | number | An identifier for the added sprite. |


SpriteBatch:addLayer

Adds a sprite to a batch created with an Array Texture.

SpriteBatch:addLayer(layerindex, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| layerindex | number | The index of the layer to use for this sprite. |
| x | number | The position to draw the sprite (x-axis). |
| y | number | The position to draw the sprite (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the added sprite, for use with SpriteBatch:set or SpriteBatch:setLayer. |

SpriteBatch:addLayer(layerindex, quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| layerindex | number | The index of the layer to use for this sprite. |
| quad | Quad | The subsection of the texture's layer to use when drawing the sprite. |
| x | number | The position to draw the sprite (x-axis). |
| y | number | The position to draw the sprite (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the added sprite, for use with SpriteBatch:set or SpriteBatch:setLayer. |

SpriteBatch:addLayer(layerindex, transform)

| name | type | description |
| --- | --- | --- |
| layerindex | number | The index of the layer to use for this sprite. |
| transform | Transform | A transform object. |

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the added sprite, for use with SpriteBatch:set or SpriteBatch:setLayer. |

SpriteBatch:addLayer(layerindex, quad, transform)

| name | type | description |
| --- | --- | --- |
| layerindex | number | The index of the layer to use for this sprite. |
| quad | Quad | The subsection of the texture's layer to use when drawing the sprite. |
| transform | Transform | A transform object. |

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the added sprite, for use with SpriteBatch:set or SpriteBatch:setLayer. |


SpriteBatch:attachAttribute

Attaches a per-vertex attribute from a Mesh onto this SpriteBatch, for use when drawing. This can be combined with a Shader to augment a SpriteBatch with per-vertex or additional per-sprite information instead of just having per-sprite colors.

Each sprite in a SpriteBatch has 4 vertices in the following order: top-left, bottom-left, top-right, bottom-right. The index returned by SpriteBatch:add (and used by SpriteBatch:set) can used to determine the first vertex of a specific sprite with the formula 1 + 4 * ( id - 1 ).

SpriteBatch:attachAttribute(name, mesh)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the vertex attribute to attach. |
| mesh | Mesh | The Mesh to get the vertex attribute from. |


SpriteBatch:clear

Removes all sprites from the buffer.

SpriteBatch:clear()


SpriteBatch:flush

Immediately sends all new and modified sprite data in the batch to the graphics card.

Normally it isn't necessary to call this method as love.graphics.draw(spritebatch, ...) will do it automatically if needed, but explicitly using SpriteBatch:flush gives more control over when the work happens.

If this method is used, it generally shouldn't be called more than once (at most) between love.graphics.draw(spritebatch, ...) calls.

SpriteBatch:flush()


SpriteBatch:getBufferSize

Gets the maximum number of sprites the SpriteBatch can hold.

SpriteBatch:getBufferSize()

| name | type | description |
| --- | --- | --- |
| size | number | The maximum number of sprites the batch can hold. |


SpriteBatch:getColor

Gets the color that will be used for the next add and set operations.

If no color has been set with SpriteBatch:setColor or the current SpriteBatch color has been cleared, this method will return nil.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

SpriteBatch:getColor()

| name | type | description |
| --- | --- | --- |
| r | number | The red component (0-1). |
| g | number | The green component (0-1). |
| b | number | The blue component (0-1). |
| a | number | The alpha component (0-1). |


SpriteBatch:getCount

Gets the number of sprites currently in the SpriteBatch.

SpriteBatch:getCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of sprites currently in the batch. |


SpriteBatch:getTexture

Gets the texture (Image or Canvas) used by the SpriteBatch.

SpriteBatch:getTexture()

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Image or Canvas used by the SpriteBatch. |


SpriteBatch:set

Changes a sprite in the batch. This requires the sprite index returned by SpriteBatch:add or SpriteBatch:addLayer.

SpriteBatch:set(spriteindex, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the sprite that will be changed. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shear factor (x-axis). |
| ky | number | Shear factor (y-axis). |

SpriteBatch:set(spriteindex, quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the sprite that will be changed. |
| quad | Quad | The Quad used on the image of the batch. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shear factor (x-axis). |
| ky | number | Shear factor (y-axis). |


SpriteBatch:setColor

Sets the color that will be used for the next add and set operations. Calling the function without arguments will disable all per-sprite colors for the SpriteBatch.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

In version 0.9.2 and older, the global color set with love.graphics.setColor will not work on the SpriteBatch if any of the sprites has its own color.

SpriteBatch:setColor(r, g, b, a)

| name | type | description |
| --- | --- | --- |
| r | number | The amount of red. |
| g | number | The amount of green. |
| b | number | The amount of blue. |
| a | number | The amount of alpha. |

SpriteBatch:setColor()


SpriteBatch:setDrawRange

Restricts the drawn sprites in the SpriteBatch to a subset of the total.

SpriteBatch:setDrawRange(start, count)

| name | type | description |
| --- | --- | --- |
| start | number | The index of the first sprite to draw. Index 1 corresponds to the first sprite added with SpriteBatch:add. |
| count | number | The number of sprites to draw. |

SpriteBatch:setDrawRange()


SpriteBatch:setLayer

Changes a sprite previously added with add or addLayer, in a batch created with an Array Texture.

SpriteBatch:setLayer(spriteindex, layerindex, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the existing sprite to replace. |
| layerindex | number | The index of the layer in the Array Texture to use for this sprite. |
| x | number | The position to draw the sprite (x-axis). |
| y | number | The position to draw the sprite (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

SpriteBatch:setLayer(spriteindex, layerindex, quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the existing sprite to replace. |
| layerindex | number | The index of the layer to use for this sprite. |
| quad | Quad | The subsection of the texture's layer to use when drawing the sprite. |
| x | number | The position to draw the sprite (x-axis). |
| y | number | The position to draw the sprite (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

SpriteBatch:setLayer(spriteindex, layerindex, transform)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the existing sprite to replace. |
| layerindex | number | The index of the layer to use for the sprite. |
| transform | Transform | A transform object. |

SpriteBatch:setLayer(spriteindex, layerindex, quad, transform)

| name | type | description |
| --- | --- | --- |
| spriteindex | number | The index of the existing sprite to replace. |
| layerindex | number | The index of the layer to use for the sprite. |
| quad | Quad | The subsection of the texture's layer to use when drawing the sprite. |
| transform | Transform | A transform object. |


SpriteBatch:setTexture

Sets the texture (Image or Canvas) used for the sprites in the batch, when drawing.

SpriteBatch:setTexture(texture)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The new Image or Canvas to use for the sprites in the batch. |


Text:add

Adds additional colored text to the Text object at the specified position.

Text:add(textstring, x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| textstring | string | The text to add to the object. |
| x | number | The position of the new text on the x-axis. |
| y | number | The position of the new text on the y-axis. |
| angle | number | The orientation of the new text in radians. |
| sx | number | Scale factor on the x-axis. |
| sy | number | Scale factor on the y-axis. |
| ox | number | Origin offset on the x-axis. |
| oy | number | Origin offset on the y-axis. |
| kx | number | Shearing / skew factor on the x-axis. |
| ky | number | Shearing / skew factor on the y-axis. |

| name | type | description |
| --- | --- | --- |
| index | number | An index number that can be used with Text:getWidth or Text:getHeight. |

Text:add(coloredtext, x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| x | number | The position of the new text on the x-axis. |
| y | number | The position of the new text on the y-axis. |
| angle | number | The orientation of the new text in radians. |
| sx | number | Scale factor on the x-axis. |
| sy | number | Scale factor on the y-axis. |
| ox | number | Origin offset on the x-axis. |
| oy | number | Origin offset on the y-axis. |
| kx | number | Shearing / skew factor on the x-axis. |
| ky | number | Shearing / skew factor on the y-axis. |

| name | type | description |
| --- | --- | --- |
| index | number | An index number that can be used with Text:getWidth or Text:getHeight. |


Text:addf

Adds additional formatted / colored text to the Text object at the specified position.

The word wrap limit is applied before any scaling, rotation, and other coordinate transformations. Therefore the amount of text per line stays constant given the same wrap limit, even if the scale arguments change.

Text:addf(textstring, wraplimit, align, x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| textstring | string | The text to add to the object. |
| wraplimit | number | The maximum width in pixels of the text before it gets automatically wrapped to a new line. |
| align | AlignMode | The alignment of the text. |
| x | number | The position of the new text (x-axis). |
| y | number | The position of the new text (y-axis). |
| angle | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing / skew factor (x-axis). |
| ky | number | Shearing / skew factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| index | number | An index number that can be used with Text:getWidth or Text:getHeight. |

Text:addf(coloredtext, wraplimit, align, x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| wraplimit | number | The maximum width in pixels of the text before it gets automatically wrapped to a new line. |
| align | AlignMode | The alignment of the text. |
| x | number | The position of the new text (x-axis). |
| y | number | The position of the new text (y-axis). |
| angle | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing / skew factor (x-axis). |
| ky | number | Shearing / skew factor (y-axis). |

| name | type | description |
| --- | --- | --- |
| index | number | An index number that can be used with Text:getWidth or Text:getHeight. |


Text:clear

Clears the contents of the Text object.

Text:clear()


Text:getDimensions

Gets the width and height of the text in pixels.

Text:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the text. If multiple sub-strings have been added with Text:add, the width of the last sub-string is returned. |
| height | number | The height of the text. If multiple sub-strings have been added with Text:add, the height of the last sub-string is returned. |

Text:getDimensions(index)

| name | type | description |
| --- | --- | --- |
| index | number | An index number returned by Text:add or Text:addf. |

| name | type | description |
| --- | --- | --- |
| width | number | The width of the sub-string (before scaling and other transformations). |
| height | number | The height of the sub-string (before scaling and other transformations). |


Text:getFont

Gets the Font used with the Text object.

Text:getFont()

| name | type | description |
| --- | --- | --- |
| font | Font | The font used with this Text object. |


Text:getHeight

Gets the height of the text in pixels.

Text:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the text. If multiple sub-strings have been added with Text:add, the height of the last sub-string is returned. |

Text:getHeight(index)

| name | type | description |
| --- | --- | --- |
| index | number | An index number returned by Text:add or Text:addf. |

| name | type | description |
| --- | --- | --- |
| height | number | The height of the sub-string (before scaling and other transformations). |


Text:getWidth

Gets the width of the text in pixels.

Text:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the text. If multiple sub-strings have been added with Text:add, the width of the last sub-string is returned. |

Text:getWidth(index)

| name | type | description |
| --- | --- | --- |
| index | number | An index number returned by Text:add or Text:addf. |

| name | type | description |
| --- | --- | --- |
| width | number | The width of the sub-string (before scaling and other transformations). |


Text:set

Replaces the contents of the Text object with a new unformatted string.

Text:set(textstring)

| name | type | description |
| --- | --- | --- |
| textstring | string | The new string of text to use. |

Text:set(coloredtext)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to use as the new text, in the form of {color1, string1, color2, string2, ...}. |


Text:setFont

Replaces the Font used with the text.

Text:setFont(font)

| name | type | description |
| --- | --- | --- |
| font | Font | The new font to use with this Text object. |


Text:setf

Replaces the contents of the Text object with a new formatted string.

Text:setf(textstring, wraplimit, align)

| name | type | description |
| --- | --- | --- |
| textstring | string | The new string of text to use. |
| wraplimit | number | The maximum width in pixels of the text before it gets automatically wrapped to a new line. |
| align | AlignMode | The alignment of the text. |

Text:setf(coloredtext, wraplimit, align)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to use as the new text, in the form of {color1, string1, color2, string2, ...}. |
| wraplimit | number | The maximum width in pixels of the text before it gets automatically wrapped to a new line. |
| align | AlignMode | The alignment of the text. |


Texture:getDPIScale

Gets the DPI scale factor of the Texture.

The DPI scale factor represents relative pixel density. A DPI scale factor of 2 means the texture has twice the pixel density in each dimension (4 times as many pixels in the same area) compared to a texture with a DPI scale factor of 1.

For example, a texture with pixel dimensions of 100x100 with a DPI scale factor of 2 will be drawn as if it was 50x50. This is useful with high-dpi /  retina displays to easily allow swapping out higher or lower pixel density Images and Canvases without needing any extra manual scaling logic.

Texture:getDPIScale()

| name | type | description |
| --- | --- | --- |
| dpiscale | number | The DPI scale factor of the Texture. |


Texture:getDepth

Gets the depth of a Volume Texture. Returns 1 for 2D, Cubemap, and Array textures.

Texture:getDepth()

| name | type | description |
| --- | --- | --- |
| depth | number | The depth of the volume Texture. |


Texture:getDepthSampleMode

Gets the comparison mode used when sampling from a depth texture in a shader.

Depth texture comparison modes are advanced low-level functionality typically used with shadow mapping in 3D.

Texture:getDepthSampleMode()

| name | type | description |
| --- | --- | --- |
| compare | CompareMode | The comparison mode used when sampling from this texture in a shader, or nil if setDepthSampleMode has not been called on this Texture. |


Texture:getDimensions

Gets the width and height of the Texture.

Texture:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the Texture. |
| height | number | The height of the Texture. |


Texture:getFilter

Gets the filter mode of the Texture.

Texture:getFilter()

| name | type | description |
| --- | --- | --- |
| min | FilterMode | Filter mode to use when minifying the texture (rendering it at a smaller size on-screen than its size in pixels). |
| mag | FilterMode | Filter mode to use when magnifying the texture (rendering it at a smaller size on-screen than its size in pixels). |
| anisotropy | number | Maximum amount of anisotropic filtering used. |


Texture:getFormat

Gets the pixel format of the Texture.

Texture:getFormat()

| name | type | description |
| --- | --- | --- |
| format | PixelFormat | The pixel format the Texture was created with. |


Texture:getHeight

Gets the height of the Texture.

Texture:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the Texture. |


Texture:getLayerCount

Gets the number of layers / slices in an Array Texture. Returns 1 for 2D, Cubemap, and Volume textures.

Texture:getLayerCount()

| name | type | description |
| --- | --- | --- |
| layers | number | The number of layers in the Array Texture. |


Texture:getMipmapCount

Gets the number of mipmaps contained in the Texture. If the texture was not created with mipmaps, it will return 1.

Texture:getMipmapCount()

| name | type | description |
| --- | --- | --- |
| mipmaps | number | The number of mipmaps in the Texture. |


Texture:getMipmapFilter

Gets the mipmap filter mode for a Texture. Prior to 11.0 this method only worked on Images.

Texture:getMipmapFilter()

| name | type | description |
| --- | --- | --- |
| mode | FilterMode | The filter mode used in between mipmap levels. nil if mipmap filtering is not enabled. |
| sharpness | number | Value used to determine whether the image should use more or less detailed mipmap levels than normal when drawing. |


Texture:getPixelDimensions

Gets the width and height in pixels of the Texture.

Texture:getDimensions gets the dimensions of the texture in units scaled by the texture's DPI scale factor, rather than pixels. Use getDimensions for calculations related to drawing the texture (calculating an origin offset, for example), and getPixelDimensions only when dealing specifically with pixels, for example when using Canvas:newImageData.

Texture:getPixelDimensions()

| name | type | description |
| --- | --- | --- |
| pixelwidth | number | The width of the Texture, in pixels. |
| pixelheight | number | The height of the Texture, in pixels. |


Texture:getPixelHeight

Gets the height in pixels of the Texture.

DPI scale factor, rather than pixels. Use getHeight for calculations related to drawing the texture (calculating an origin offset, for example), and getPixelHeight only when dealing specifically with pixels, for example when using Canvas:newImageData.

Texture:getPixelHeight()

| name | type | description |
| --- | --- | --- |
| pixelheight | number | The height of the Texture, in pixels. |


Texture:getPixelWidth

Gets the width in pixels of the Texture.

DPI scale factor, rather than pixels. Use getWidth for calculations related to drawing the texture (calculating an origin offset, for example), and getPixelWidth only when dealing specifically with pixels, for example when using Canvas:newImageData.

Texture:getPixelWidth()

| name | type | description |
| --- | --- | --- |
| pixelwidth | number | The width of the Texture, in pixels. |


Texture:getTextureType

Gets the type of the Texture.

Texture:getTextureType()

| name | type | description |
| --- | --- | --- |
| texturetype | TextureType | The type of the Texture. |


Texture:getWidth

Gets the width of the Texture.

Texture:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the Texture. |


Texture:getWrap

Gets the wrapping properties of a Texture.

This function returns the currently set horizontal and vertical wrapping modes for the texture.

Texture:getWrap()

| name | type | description |
| --- | --- | --- |
| horiz | WrapMode | Horizontal wrapping mode of the texture. |
| vert | WrapMode | Vertical wrapping mode of the texture. |
| depth | WrapMode | Wrapping mode for the z-axis of a Volume texture. |


Texture:isReadable

Gets whether the Texture can be drawn and sent to a Shader.

Canvases created with stencil and/or depth PixelFormats are not readable by default, unless readable=true is specified in the settings table passed into love.graphics.newCanvas.

Non-readable Canvases can still be rendered to.

Texture:isReadable()

| name | type | description |
| --- | --- | --- |
| readable | boolean | Whether the Texture is readable. |


Texture:setDepthSampleMode

Sets the comparison mode used when sampling from a depth texture in a shader. Depth texture comparison modes are advanced low-level functionality typically used with shadow mapping in 3D.

When using a depth texture with a comparison mode set in a shader, it must be declared as a sampler2DShadow and used in a GLSL 3 Shader. The result of accessing the texture in the shader will return a float between 0 and 1, proportional to the number of samples (up to 4 samples will be used if bilinear filtering is enabled) that passed the test set by the comparison operation.

Depth texture comparison can only be used with readable depth-formatted Canvases.

Texture:setDepthSampleMode(compare)

| name | type | description |
| --- | --- | --- |
| compare | CompareMode | The comparison mode used when sampling from this texture in a shader. |


Texture:setFilter

Sets the filter mode of the Texture.

Texture:setFilter(min, mag, anisotropy)

| name | type | description |
| --- | --- | --- |
| min | FilterMode | Filter mode to use when minifying the texture (rendering it at a smaller size on-screen than its size in pixels). |
| mag | FilterMode | Filter mode to use when magnifying the texture (rendering it at a larger size on-screen than its size in pixels). |
| anisotropy | number | Maximum amount of anisotropic filtering to use. |


Texture:setMipmapFilter

Sets the mipmap filter mode for a Texture. Prior to 11.0 this method only worked on Images.

Mipmapping is useful when drawing a texture at a reduced scale. It can improve performance and reduce aliasing issues.

In created with the mipmaps flag enabled for the mipmap filter to have any effect. In versions prior to 0.10.0 it's best to call this method directly after creating the image with love.graphics.newImage, to avoid bugs in certain graphics drivers.

Due to hardware restrictions and driver bugs, in versions prior to 0.10.0 images that weren't loaded from a CompressedData must have power-of-two dimensions (64x64, 512x256, etc.) to use mipmaps.

Texture:setMipmapFilter(filtermode, sharpness)

| name | type | description |
| --- | --- | --- |
| filtermode | FilterMode | The filter mode to use in between mipmap levels. 'nearest' will often give better performance. |
| sharpness | number | A positive sharpness value makes the texture use a more detailed mipmap level when drawing, at the expense of performance. A negative value does the reverse. |

Texture:setMipmapFilter()


Texture:setWrap

Sets the wrapping properties of a Texture.

This function sets the way a Texture is repeated when it is drawn with a Quad that is larger than the texture's extent, or when a custom Shader is used which uses texture coordinates outside of [0, 1]. A texture may be clamped or set to repeat in both horizontal and vertical directions.

Clamped textures appear only once (with the edges of the texture stretching to fill the extent of the Quad), whereas repeated ones repeat as many times as there is room in the Quad.

Texture:setWrap(horiz, vert, depth)

| name | type | description |
| --- | --- | --- |
| horiz | WrapMode | Horizontal wrapping mode of the texture. |
| vert | WrapMode | Vertical wrapping mode of the texture. |
| depth | WrapMode | Wrapping mode for the z-axis of a Volume texture. |


Thread:getError

Retrieves the error string from the thread if it produced an error.

Thread:getError()

| name | type | description |
| --- | --- | --- |
| err | string | The error message, or nil if the Thread has not caused an error. |


Thread:isRunning

Returns whether the thread is currently running.

Threads which are not running can be (re)started with Thread:start.

Thread:isRunning()

| name | type | description |
| --- | --- | --- |
| value | boolean | True if the thread is running, false otherwise. |


Thread:start

Starts the thread.

Beginning with version 0.9.0, threads can be restarted after they have completed their execution.

Thread:start()

Thread:start(...)

| name | type | description |
| --- | --- | --- |
| ... | Variant | A string, number, boolean, LÖVE object, or simple table. |


Thread:wait

Wait for a thread to finish.

This call will block until the thread finishes.

Thread:wait()


Transform:apply

Applies the given other Transform object to this one.

This effectively multiplies this Transform's internal transformation matrix with the other Transform's (i.e. self * other), and stores the result in this object.

Transform:apply(other)

| name | type | description |
| --- | --- | --- |
| other | Transform | The other Transform object to apply to this Transform. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:clone

Creates a new copy of this Transform.

Transform:clone()

| name | type | description |
| --- | --- | --- |
| clone | Transform | The copy of this Transform. |


Transform:getMatrix

Gets the internal 4x4 transformation matrix stored by this Transform. The matrix is returned in row-major order.

Transform:getMatrix()

| name | type | description |
| --- | --- | --- |
| e1_1 | number | The first column of the first row of the matrix. |
| e1_2 | number | The second column of the first row of the matrix. |
| e1_3 | number | The third column of the first row of the matrix. |
| e1_4 | number | The fourth column of the first row of the matrix. |
| e2_1 | number | The first column of the second row of the matrix. |
| e2_2 | number | The second column of the second row of the matrix. |
| e2_3 | number | The third column of the second row of the matrix. |
| e2_4 | number | The fourth column of the second row of the matrix. |
| e3_1 | number | The first column of the third row of the matrix. |
| e3_2 | number | The second column of the third row of the matrix. |
| e3_3 | number | The third column of the third row of the matrix. |
| e3_4 | number | The fourth column of the third row of the matrix. |
| e4_1 | number | The first column of the fourth row of the matrix. |
| e4_2 | number | The second column of the fourth row of the matrix. |
| e4_3 | number | The third column of the fourth row of the matrix. |
| e4_4 | number | The fourth column of the fourth row of the matrix. |


Transform:inverse

Creates a new Transform containing the inverse of this Transform.

Transform:inverse()

| name | type | description |
| --- | --- | --- |
| inverse | Transform | A new Transform object representing the inverse of this Transform's matrix. |


Transform:inverseTransformPoint

Applies the reverse of the Transform object's transformation to the given 2D position.

This effectively converts the given position from the local coordinate space of the Transform into global coordinates.

One use of this method can be to convert a screen-space mouse position into global world coordinates, if the given Transform has transformations applied that are used for a camera system in-game.

Transform:inverseTransformPoint(localX, localY)

| name | type | description |
| --- | --- | --- |
| localX | number | The x component of the position with the transform applied. |
| localY | number | The y component of the position with the transform applied. |

| name | type | description |
| --- | --- | --- |
| globalX | number | The x component of the position in global coordinates. |
| globalY | number | The y component of the position in global coordinates. |


Transform:isAffine2DTransform

Checks whether the Transform is an affine transformation.

Transform:isAffine2DTransform()

| name | type | description |
| --- | --- | --- |
| affine | boolean | true if the transform object is an affine transformation, false otherwise. |


Transform:reset

Resets the Transform to an identity state. All previously applied transformations are erased.

Transform:reset()

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:rotate

Applies a rotation to the Transform's coordinate system. This method does not reset any previously applied transformations.

Transform:rotate(angle)

| name | type | description |
| --- | --- | --- |
| angle | number | The relative angle in radians to rotate this Transform by. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:scale

Scales the Transform's coordinate system. This method does not reset any previously applied transformations.

Transform:scale(sx, sy)

| name | type | description |
| --- | --- | --- |
| sx | number | The relative scale factor along the x-axis. |
| sy | number | The relative scale factor along the y-axis. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:setMatrix

Directly sets the Transform's internal 4x4 transformation matrix.

Transform:setMatrix(e1_1, e1_2, e1_3, e1_4, e2_1, e2_2, e2_3, e2_4, e3_1, e3_2, e3_3, e3_4, e4_1, e4_2, e4_3, e4_4)

| name | type | description |
| --- | --- | --- |
| e1_1 | number | The first column of the first row of the matrix. |
| e1_2 | number | The second column of the first row of the matrix. |
| e1_3 | number | The third column of the first row of the matrix. |
| e1_4 | number | The fourth column of the first row of the matrix. |
| e2_1 | number | The first column of the second row of the matrix. |
| e2_2 | number | The second column of the second row of the matrix. |
| e2_3 | number | The third column of the second row of the matrix. |
| e2_4 | number | The fourth column of the second row of the matrix. |
| e3_1 | number | The first column of the third row of the matrix. |
| e3_2 | number | The second column of the third row of the matrix. |
| e3_3 | number | The third column of the third row of the matrix. |
| e3_4 | number | The fourth column of the third row of the matrix. |
| e4_1 | number | The first column of the fourth row of the matrix. |
| e4_2 | number | The second column of the fourth row of the matrix. |
| e4_3 | number | The third column of the fourth row of the matrix. |
| e4_4 | number | The fourth column of the fourth row of the matrix. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |

Transform:setMatrix(layout, e1_1, e1_2, e1_3, e1_4, e2_1, e2_2, e2_3, e2_4, e3_1, e3_2, e3_3, e3_4, e4_1, e4_2, e4_3, e4_4)

| name | type | description |
| --- | --- | --- |
| layout | MatrixLayout | How to interpret the matrix element arguments (row-major or column-major). |
| e1_1 | number | The first column of the first row of the matrix. |
| e1_2 | number | The second column of the first row or the first column of the second row of the matrix, depending on the specified layout. |
| e1_3 | number | The third column/row of the first row/column of the matrix. |
| e1_4 | number | The fourth column/row of the first row/column of the matrix. |
| e2_1 | number | The first column/row of the second row/column of the matrix. |
| e2_2 | number | The second column/row of the second row/column of the matrix. |
| e2_3 | number | The third column/row of the second row/column of the matrix. |
| e2_4 | number | The fourth column/row of the second row/column of the matrix. |
| e3_1 | number | The first column/row of the third row/column of the matrix. |
| e3_2 | number | The second column/row of the third row/column of the matrix. |
| e3_3 | number | The third column/row of the third row/column of the matrix. |
| e3_4 | number | The fourth column/row of the third row/column of the matrix. |
| e4_1 | number | The first column/row of the fourth row/column of the matrix. |
| e4_2 | number | The second column/row of the fourth row/column of the matrix. |
| e4_3 | number | The third column/row of the fourth row/column of the matrix. |
| e4_4 | number | The fourth column of the fourth row of the matrix. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |

Transform:setMatrix(layout, matrix)

| name | type | description |
| --- | --- | --- |
| layout | MatrixLayout | How to interpret the matrix element arguments (row-major or column-major). |
| matrix | table | A flat table containing the 16 matrix elements. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |

Transform:setMatrix(layout, matrix)

| name | type | description |
| --- | --- | --- |
| layout | MatrixLayout | How to interpret the matrix element arguments (row-major or column-major). |
| matrix | table | A table of 4 tables, with each sub-table containing 4 matrix elements. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:setTransformation

Resets the Transform to the specified transformation parameters.

Transform:setTransformation(x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the Transform on the x-axis. |
| y | number | The position of the Transform on the y-axis. |
| angle | number | The orientation of the Transform in radians. |
| sx | number | Scale factor on the x-axis. |
| sy | number | Scale factor on the y-axis. |
| ox | number | Origin offset on the x-axis. |
| oy | number | Origin offset on the y-axis. |
| kx | number | Shearing / skew factor on the x-axis. |
| ky | number | Shearing / skew factor on the y-axis. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:shear

Applies a shear factor (skew) to the Transform's coordinate system. This method does not reset any previously applied transformations.

Transform:shear(kx, ky)

| name | type | description |
| --- | --- | --- |
| kx | number | The shear factor along the x-axis. |
| ky | number | The shear factor along the y-axis. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Transform:transformPoint

Applies the Transform object's transformation to the given 2D position.

This effectively converts the given position from global coordinates into the local coordinate space of the Transform.

Transform:transformPoint(globalX, globalY)

| name | type | description |
| --- | --- | --- |
| globalX | number | The x component of the position in global coordinates. |
| globalY | number | The y component of the position in global coordinates. |

| name | type | description |
| --- | --- | --- |
| localX | number | The x component of the position with the transform applied. |
| localY | number | The y component of the position with the transform applied. |


Transform:translate

Applies a translation to the Transform's coordinate system. This method does not reset any previously applied transformations.

Transform:translate(dx, dy)

| name | type | description |
| --- | --- | --- |
| dx | number | The relative translation along the x-axis. |
| dy | number | The relative translation along the y-axis. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object the method was called on. Allows easily chaining Transform methods. |


Video:getDimensions

Gets the width and height of the Video in pixels.

Video:getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the Video. |
| height | number | The height of the Video. |


Video:getFilter

Gets the scaling filters used when drawing the Video.

Video:getFilter()

| name | type | description |
| --- | --- | --- |
| min | FilterMode | The filter mode used when scaling the Video down. |
| mag | FilterMode | The filter mode used when scaling the Video up. |
| anisotropy | number | Maximum amount of anisotropic filtering used. |


Video:getHeight

Gets the height of the Video in pixels.

Video:getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the Video. |


Video:getSource

Gets the audio Source used for playing back the video's audio. May return nil if the video has no audio, or if Video:setSource is called with a nil argument.

Video:getSource()

| name | type | description |
| --- | --- | --- |
| source | Source | The audio Source used for audio playback, or nil if the video has no audio. |


Video:getStream

Gets the VideoStream object used for decoding and controlling the video.

Video:getStream()

| name | type | description |
| --- | --- | --- |
| stream | VideoStream | The VideoStream used for decoding and controlling the video. |


Video:getWidth

Gets the width of the Video in pixels.

Video:getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the Video. |


Video:isPlaying

Gets whether the Video is currently playing.

Video:isPlaying()

| name | type | description |
| --- | --- | --- |
| playing | boolean | Whether the video is playing. |


Video:pause

Pauses the Video.

Video:pause()


Video:play

Starts playing the Video. In order for the video to appear onscreen it must be drawn with love.graphics.draw.

Video:play()


Video:rewind

Rewinds the Video to the beginning.

Video:rewind()


Video:seek

Sets the current playback position of the Video.

Video:seek(offset)

| name | type | description |
| --- | --- | --- |
| offset | number | The time in seconds since the beginning of the Video. |


Video:setFilter

Sets the scaling filters used when drawing the Video.

Video:setFilter(min, mag, anisotropy)

| name | type | description |
| --- | --- | --- |
| min | FilterMode | The filter mode used when scaling the Video down. |
| mag | FilterMode | The filter mode used when scaling the Video up. |
| anisotropy | number | Maximum amount of anisotropic filtering used. |


Video:setSource

Sets the audio Source used for playing back the video's audio. The audio Source also controls playback speed and synchronization.

Video:setSource(source)

| name | type | description |
| --- | --- | --- |
| source | Source | The audio Source used for audio playback, or nil to disable audio synchronization. |


Video:tell

Gets the current playback position of the Video.

Video:tell()

| name | type | description |
| --- | --- | --- |
| seconds | number | The time in seconds since the beginning of the Video. |


VideoStream:getFilename

Gets the filename of the VideoStream.

VideoStream:getFilename()

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the VideoStream |


VideoStream:isPlaying

Gets whether the VideoStream is playing.

VideoStream:isPlaying()

| name | type | description |
| --- | --- | --- |
| playing | boolean | Whether the VideoStream is playing. |


VideoStream:pause

Pauses the VideoStream.

VideoStream:pause()


VideoStream:play

Plays the VideoStream.

VideoStream:play()


VideoStream:rewind

Rewinds the VideoStream. Synonym to VideoStream:seek(0).

VideoStream:rewind()


VideoStream:seek

Sets the current playback position of the VideoStream.

VideoStream:seek(offset)

| name | type | description |
| --- | --- | --- |
| offset | number | The time in seconds since the beginning of the VideoStream. |


VideoStream:tell

Gets the current playback position of the VideoStream.

VideoStream:tell()

| name | type | description |
| --- | --- | --- |
| seconds | number | The number of seconds sionce the beginning of the VideoStream. |


WeldJoint:getDampingRatio

Returns the damping ratio of the joint.

WeldJoint:getDampingRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The damping ratio. |


WeldJoint:getFrequency

Returns the frequency.

WeldJoint:getFrequency()

| name | type | description |
| --- | --- | --- |
| freq | number | The frequency in hertz. |


WeldJoint:getReferenceAngle

Gets the reference angle.

WeldJoint:getReferenceAngle()

| name | type | description |
| --- | --- | --- |
| angle | number | The reference angle in radians. |


WeldJoint:setDampingRatio

Sets a new damping ratio.

WeldJoint:setDampingRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The new damping ratio. |


WeldJoint:setFrequency

Sets a new frequency.

WeldJoint:setFrequency(freq)

| name | type | description |
| --- | --- | --- |
| freq | number | The new frequency in hertz. |


WheelJoint:getAxis

Gets the world-space axis vector of the Wheel Joint.

WheelJoint:getAxis()

| name | type | description |
| --- | --- | --- |
| x | number | The x-axis coordinate of the world-space axis vector. |
| y | number | The y-axis coordinate of the world-space axis vector. |


WheelJoint:getJointSpeed

Returns the current joint translation speed.

WheelJoint:getJointSpeed()

| name | type | description |
| --- | --- | --- |
| speed | number | The translation speed of the joint in meters per second. |


WheelJoint:getJointTranslation

Returns the current joint translation.

WheelJoint:getJointTranslation()

| name | type | description |
| --- | --- | --- |
| position | number | The translation of the joint in meters. |


WheelJoint:getMaxMotorTorque

Returns the maximum motor torque.

WheelJoint:getMaxMotorTorque()

| name | type | description |
| --- | --- | --- |
| maxTorque | number | The maximum torque of the joint motor in newton meters. |


WheelJoint:getMotorSpeed

Returns the speed of the motor.

WheelJoint:getMotorSpeed()

| name | type | description |
| --- | --- | --- |
| speed | number | The speed of the joint motor in radians per second. |


WheelJoint:getMotorTorque

Returns the current torque on the motor.

WheelJoint:getMotorTorque(invdt)

| name | type | description |
| --- | --- | --- |
| invdt | number | How long the force applies. Usually the inverse time step or 1/dt. |

| name | type | description |
| --- | --- | --- |
| torque | number | The torque on the motor in newton meters. |


WheelJoint:getSpringDampingRatio

Returns the damping ratio.

WheelJoint:getSpringDampingRatio()

| name | type | description |
| --- | --- | --- |
| ratio | number | The damping ratio. |


WheelJoint:getSpringFrequency

Returns the spring frequency.

WheelJoint:getSpringFrequency()

| name | type | description |
| --- | --- | --- |
| freq | number | The frequency in hertz. |


WheelJoint:isMotorEnabled

Checks if the joint motor is running.

WheelJoint:isMotorEnabled()

| name | type | description |
| --- | --- | --- |
| on | boolean | The status of the joint motor. |


WheelJoint:setMaxMotorTorque

Sets a new maximum motor torque.

WheelJoint:setMaxMotorTorque(maxTorque)

| name | type | description |
| --- | --- | --- |
| maxTorque | number | The new maximum torque for the joint motor in newton meters. |


WheelJoint:setMotorEnabled

Starts and stops the joint motor.

WheelJoint:setMotorEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True turns the motor on and false turns it off. |


WheelJoint:setMotorSpeed

Sets a new speed for the motor.

WheelJoint:setMotorSpeed(speed)

| name | type | description |
| --- | --- | --- |
| speed | number | The new speed for the joint motor in radians per second. |


WheelJoint:setSpringDampingRatio

Sets a new damping ratio.

WheelJoint:setSpringDampingRatio(ratio)

| name | type | description |
| --- | --- | --- |
| ratio | number | The new damping ratio. |


WheelJoint:setSpringFrequency

Sets a new spring frequency.

WheelJoint:setSpringFrequency(freq)

| name | type | description |
| --- | --- | --- |
| freq | number | The new frequency in hertz. |


World:destroy

Destroys the world, taking all bodies, joints, fixtures and their shapes with it.

An error will occur if you attempt to use any of the destroyed objects after calling this function.

World:destroy()


World:getBodies

Returns a table with all bodies.

World:getBodies()

| name | type | description |
| --- | --- | --- |
| bodies | table | A sequence with all bodies. |


World:getBodyCount

Returns the number of bodies in the world.

World:getBodyCount()

| name | type | description |
| --- | --- | --- |
| n | number | The number of bodies in the world. |


World:getCallbacks

Returns functions for the callbacks during the world update.

World:getCallbacks()

| name | type | description |
| --- | --- | --- |
| beginContact | function | Gets called when two fixtures begin to overlap. |
| endContact | function | Gets called when two fixtures cease to overlap. |
| preSolve | function | Gets called before a collision gets resolved. |
| postSolve | function | Gets called after the collision has been resolved. |


World:getContactCount

Returns the number of contacts in the world.

World:getContactCount()

| name | type | description |
| --- | --- | --- |
| n | number | The number of contacts in the world. |


World:getContactFilter

Returns the function for collision filtering.

World:getContactFilter()

| name | type | description |
| --- | --- | --- |
| contactFilter | function | The function that handles the contact filtering. |


World:getContacts

Returns a table with all Contacts.

World:getContacts()

| name | type | description |
| --- | --- | --- |
| contacts | table | A sequence with all Contacts. |


World:getGravity

Get the gravity of the world.

World:getGravity()

| name | type | description |
| --- | --- | --- |
| x | number | The x component of gravity. |
| y | number | The y component of gravity. |


World:getJointCount

Returns the number of joints in the world.

World:getJointCount()

| name | type | description |
| --- | --- | --- |
| n | number | The number of joints in the world. |


World:getJoints

Returns a table with all joints.

World:getJoints()

| name | type | description |
| --- | --- | --- |
| joints | table | A sequence with all joints. |


World:isDestroyed

Gets whether the World is destroyed. Destroyed worlds cannot be used.

World:isDestroyed()

| name | type | description |
| --- | --- | --- |
| destroyed | boolean | Whether the World is destroyed. |


World:isLocked

Returns if the world is updating its state.

This will return true inside the callbacks from World:setCallbacks.

World:isLocked()

| name | type | description |
| --- | --- | --- |
| locked | boolean | Will be true if the world is in the process of updating its state. |


World:isSleepingAllowed

Gets the sleep behaviour of the world.

World:isSleepingAllowed()

| name | type | description |
| --- | --- | --- |
| allow | boolean | True if bodies in the world are allowed to sleep, or false if not. |


World:queryBoundingBox

Calls a function for each fixture inside the specified area by searching for any overlapping bounding box (Fixture:getBoundingBox).

World:queryBoundingBox(topLeftX, topLeftY, bottomRightX, bottomRightY, callback)

| name | type | description |
| --- | --- | --- |
| topLeftX | number | The x position of the top-left point. |
| topLeftY | number | The y position of the top-left point. |
| bottomRightX | number | The x position of the bottom-right point. |
| bottomRightY | number | The y position of the bottom-right point. |
| callback | function | This function gets passed one argument, the fixture, and should return a boolean. The search will continue if it is true or stop if it is false. |


World:rayCast

Casts a ray and calls a function for each fixtures it intersects.

World:rayCast(x1, y1, x2, y2, callback)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the starting point of the ray. |
| y1 | number | The x position of the starting point of the ray. |
| x2 | number | The x position of the end point of the ray. |
| y2 | number | The x value of the surface normal vector of the shape edge. |
| callback | function | A function called for each fixture intersected by the ray. The function gets six arguments and should return a number as a control value. The intersection points fed into the function will be in an arbitrary order. If you wish to find the closest point of intersection, you'll need to do that yourself within the function. The easiest way to do that is by using the fraction value. |


World:setCallbacks

Sets functions for the collision callbacks during the world update.

Four Lua functions can be given as arguments. The value nil removes a function.

When called, each function will be passed three arguments. The first two arguments are the colliding fixtures and the third argument is the Contact between them. The postSolve callback additionally gets the normal and tangent impulse for each contact point. See notes.

If you are interested to know when exactly each callback is called, consult a Box2d manual

World:setCallbacks(beginContact, endContact, preSolve, postSolve)

| name | type | description |
| --- | --- | --- |
| beginContact | function | Gets called when two fixtures begin to overlap. |
| endContact | function | Gets called when two fixtures cease to overlap. This will also be called outside of a world update, when colliding objects are destroyed. |
| preSolve | function | Gets called before a collision gets resolved. |
| postSolve | function | Gets called after the collision has been resolved. |


World:setContactFilter

Sets a function for collision filtering.

If the group and category filtering doesn't generate a collision decision, this function gets called with the two fixtures as arguments. The function should return a boolean value where true means the fixtures will collide and false means they will pass through each other.

World:setContactFilter(filter)

| name | type | description |
| --- | --- | --- |
| filter | function | The function handling the contact filtering. |


World:setGravity

Set the gravity of the world.

World:setGravity(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x component of gravity. |
| y | number | The y component of gravity. |


World:setSleepingAllowed

Sets the sleep behaviour of the world.

World:setSleepingAllowed(allow)

| name | type | description |
| --- | --- | --- |
| allow | boolean | True if bodies in the world are allowed to sleep, or false if not. |


World:translateOrigin

Translates the World's origin. Useful in large worlds where floating point precision issues become noticeable at far distances from the origin.

World:translateOrigin(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x component of the new origin with respect to the old origin. |
| y | number | The y component of the new origin with respect to the old origin. |


World:update

Update the state of the world.

World:update(dt, velocityiterations, positioniterations)

| name | type | description |
| --- | --- | --- |
| dt | number | The time (in seconds) to advance the physics simulation. |
| velocityiterations | number | The maximum number of steps used to determine the new velocities when resolving a collision. |
| positioniterations | number | The maximum number of steps used to determine the new positions when resolving a collision. |


love.audio.getActiveEffects

Gets a list of the names of the currently enabled effects.

love.audio.getActiveEffects()

| name | type | description |
| --- | --- | --- |
| effects | table | The list of the names of the currently enabled effects. |


love.audio.getActiveSourceCount

Gets the current number of simultaneously playing sources.

love.audio.getActiveSourceCount()

| name | type | description |
| --- | --- | --- |
| count | number | The current number of simultaneously playing sources. |


love.audio.getDistanceModel

Returns the distance attenuation model.

love.audio.getDistanceModel()

| name | type | description |
| --- | --- | --- |
| model | DistanceModel | The current distance model. The default is 'inverseclamped'. |


love.audio.getDopplerScale

Gets the current global scale factor for velocity-based doppler effects.

love.audio.getDopplerScale()

| name | type | description |
| --- | --- | --- |
| scale | number | The current doppler scale factor. |


love.audio.getEffect

Gets the settings associated with an effect.

love.audio.getEffect(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect. |

| name | type | description |
| --- | --- | --- |
| settings | table | The settings associated with the effect. |


love.audio.getMaxSceneEffects

Gets the maximum number of active effects supported by the system.

love.audio.getMaxSceneEffects()

| name | type | description |
| --- | --- | --- |
| maximum | number | The maximum number of active effects. |


love.audio.getMaxSourceEffects

Gets the maximum number of active Effects in a single Source object, that the system can support.

love.audio.getMaxSourceEffects()

| name | type | description |
| --- | --- | --- |
| maximum | number | The maximum number of active Effects per Source. |


love.audio.getOrientation

Returns the orientation of the listener.

love.audio.getOrientation()

| name | type | description |
| --- | --- | --- |
| fx | number | Forward x of the listener orientation. |
| fy | number | Forward y of the listener orientation. |
| fz | number | Forward z of the listener orientation. |
| ux | number | Up x of the listener orientation. |
| uy | number | Up y of the listener orientation. |
| uz | number | Up z of the listener orientation. |


love.audio.getPosition

Returns the position of the listener. Please note that positional audio only works for mono (i.e. non-stereo) sources.

love.audio.getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | The X position of the listener. |
| y | number | The Y position of the listener. |
| z | number | The Z position of the listener. |


love.audio.getRecordingDevices

Gets a list of RecordingDevices on the system.

The first device in the list is the user's default recording device. The list may be empty if there are no microphones connected to the system.

Audio recording is currently not supported on iOS.

love.audio.getRecordingDevices()

| name | type | description |
| --- | --- | --- |
| devices | table | The list of connected recording devices. |


love.audio.getVelocity

Returns the velocity of the listener.

love.audio.getVelocity()

| name | type | description |
| --- | --- | --- |
| x | number | The X velocity of the listener. |
| y | number | The Y velocity of the listener. |
| z | number | The Z velocity of the listener. |


love.audio.getVolume

Returns the master volume.

love.audio.getVolume()

| name | type | description |
| --- | --- | --- |
| volume | number | The current master volume |


love.audio.isEffectsSupported

Gets whether audio effects are supported in the system.

love.audio.isEffectsSupported()

| name | type | description |
| --- | --- | --- |
| supported | boolean | True if effects are supported, false otherwise. |


love.audio.newQueueableSource

Creates a new Source usable for real-time generated sound playback with Source:queue.

love.audio.newQueueableSource(samplerate, bitdepth, channels, buffercount)

| name | type | description |
| --- | --- | --- |
| samplerate | number | Number of samples per second when playing. |
| bitdepth | number | Bits per sample (8 or 16). |
| channels | number | 1 for mono or 2 for stereo. |
| buffercount | number | The number of buffers that can be queued up at any given time with Source:queue. Cannot be greater than 64. A sensible default (~8) is chosen if no value is specified. |

| name | type | description |
| --- | --- | --- |
| source | Source | The new Source usable with Source:queue. |


love.audio.newSource

Creates a new Source from a filepath, File, Decoder or SoundData.

Sources created from SoundData are always static.

love.audio.newSource(filename, type)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the audio file. |
| type | SourceType | Streaming or static source. |

| name | type | description |
| --- | --- | --- |
| source | Source | A new Source that can play the specified audio. |

love.audio.newSource(file, type)

| name | type | description |
| --- | --- | --- |
| file | File | A File pointing to an audio file. |
| type | SourceType | Streaming or static source. |

| name | type | description |
| --- | --- | --- |
| source | Source | A new Source that can play the specified audio. |

love.audio.newSource(decoder, type)

| name | type | description |
| --- | --- | --- |
| decoder | Decoder | The Decoder to create a Source from. |
| type | SourceType | Streaming or static source. |

| name | type | description |
| --- | --- | --- |
| source | Source | A new Source that can play the specified audio. |

love.audio.newSource(data, type)

| name | type | description |
| --- | --- | --- |
| data | FileData | The FileData to create a Source from. |
| type | SourceType | Streaming or static source. |

| name | type | description |
| --- | --- | --- |
| source | Source | A new Source that can play the specified audio. |

love.audio.newSource(data)

| name | type | description |
| --- | --- | --- |
| data | SoundData | The SoundData to create a Source from. |

| name | type | description |
| --- | --- | --- |
| source | Source | A new Source that can play the specified audio. The SourceType of the returned audio is 'static'. |


love.audio.pause

Pauses specific or all currently played Sources.

love.audio.pause()

| name | type | description |
| --- | --- | --- |
| Sources | table | A table containing a list of Sources that were paused by this call. |

love.audio.pause(source, ...)

| name | type | description |
| --- | --- | --- |
| source | Source | The first Source to pause. |
| ... | Source | Additional Sources to pause. |

love.audio.pause(sources)

| name | type | description |
| --- | --- | --- |
| sources | table | A table containing a list of Sources to pause. |


love.audio.play

Plays the specified Source.

love.audio.play(source)

| name | type | description |
| --- | --- | --- |
| source | Source | The Source to play. |

love.audio.play(sources)

| name | type | description |
| --- | --- | --- |
| sources | table | Table containing a list of Sources to play. |

love.audio.play(source1, source2, ...)

| name | type | description |
| --- | --- | --- |
| source1 | Source | The first Source to play. |
| source2 | Source | The second Source to play. |
| ... | Source | Additional Sources to play. |


love.audio.setDistanceModel

Sets the distance attenuation model.

love.audio.setDistanceModel(model)

| name | type | description |
| --- | --- | --- |
| model | DistanceModel | The new distance model. |


love.audio.setDopplerScale

Sets a global scale factor for velocity-based doppler effects. The default scale value is 1.

love.audio.setDopplerScale(scale)

| name | type | description |
| --- | --- | --- |
| scale | number | The new doppler scale factor. The scale must be greater than 0. |


love.audio.setEffect

Defines an effect that can be applied to a Source.

Not all system supports audio effects. Use love.audio.isEffectsSupported to check.

love.audio.setEffect(name, settings)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect. |
| settings | table | The settings to use for this effect, with the following fields: |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the effect was successfully created. |

love.audio.setEffect(name, enabled)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the effect. |
| enabled | boolean | If false and the given effect name was previously set, disables the effect. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the effect was successfully disabled. |


love.audio.setMixWithSystem

Sets whether the system should mix the audio with the system's audio.

love.audio.setMixWithSystem(mix)

| name | type | description |
| --- | --- | --- |
| mix | boolean | True to enable mixing, false to disable it. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the change succeeded, false otherwise. |


love.audio.setOrientation

Sets the orientation of the listener.

love.audio.setOrientation(fx, fy, fz, ux, uy, uz)

| name | type | description |
| --- | --- | --- |
| fx, fy, fz | number | Forward vector of the listener orientation. |
| ux, uy, uz | number | Up vector of the listener orientation. |


love.audio.setPosition

Sets the position of the listener, which determines how sounds play.

love.audio.setPosition(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the listener. |
| y | number | The y position of the listener. |
| z | number | The z position of the listener. |


love.audio.setVelocity

Sets the velocity of the listener.

love.audio.setVelocity(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The X velocity of the listener. |
| y | number | The Y velocity of the listener. |
| z | number | The Z velocity of the listener. |


love.audio.setVolume

Sets the master volume.

love.audio.setVolume(volume)

| name | type | description |
| --- | --- | --- |
| volume | number | 1.0 is max and 0.0 is off. |


love.audio.stop

Stops currently played sources.

love.audio.stop()

love.audio.stop(source)

| name | type | description |
| --- | --- | --- |
| source | Source | The source on which to stop the playback. |

love.audio.stop(source1, source2, ...)

| name | type | description |
| --- | --- | --- |
| source1 | Source | The first Source to stop. |
| source2 | Source | The second Source to stop. |
| ... | Source | Additional Sources to stop. |

love.audio.stop(sources)

| name | type | description |
| --- | --- | --- |
| sources | table | A table containing a list of Sources to stop. |


love.conf

If a file called conf.lua is present in your game folder (or .love file), it is run before the LÖVE modules are loaded. You can use this file to overwrite the love.conf function, which is later called by the LÖVE 'boot' script. Using the love.conf function, you can set some configuration options, and change things like the default size of the window, which modules are loaded, and other stuff.

love.conf(t)

| name | type | description |
| --- | --- | --- |
| t | table | The love.conf function takes one argument: a table filled with all the default values which you can overwrite to your liking. If you want to change the default window size, for instance, do: function love.conf(t)     t.window.width = 1024     t.window.height = 768 end If you don't need the physics module or joystick module, do the following. function love.conf(t)     t.modules.joystick = false     t.modules.physics = false end Setting unused modules to false is encouraged when you release your game. It reduces startup time slightly (especially if the joystick module is disabled) and reduces memory usage (slightly). Note that you can't disable love.filesystem; it's mandatory. The same goes for the love module itself. love.graphics needs love.window to be enabled. |


love.data.compress

Compresses a string or data using a specific compression algorithm.

love.data.compress(container, format, rawstring, level)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the compressed data as. |
| format | CompressedDataFormat | The format to use when compressing the string. |
| rawstring | string | The raw (un-compressed) string to compress. |
| level | number | The level of compression to use, between 0 and 9. -1 indicates the default level. The meaning of this argument depends on the compression format being used. |

| name | type | description |
| --- | --- | --- |
| compressedData | CompressedData or string | CompressedData/string which contains the compressed version of rawstring. |

love.data.compress(container, format, data, level)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the compressed data as. |
| format | CompressedDataFormat | The format to use when compressing the data. |
| data | Data | A Data object containing the raw (un-compressed) data to compress. |
| level | number | The level of compression to use, between 0 and 9. -1 indicates the default level. The meaning of this argument depends on the compression format being used. |

| name | type | description |
| --- | --- | --- |
| compressedData | CompressedData or string | CompressedData/string which contains the compressed version of data. |


love.data.decode

Decode Data or a string from any of the EncodeFormats to Data or string.

love.data.decode(container, format, sourceString)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the decoded data as. |
| format | EncodeFormat | The format of the input data. |
| sourceString | string | The raw (encoded) data to decode. |

| name | type | description |
| --- | --- | --- |
| decoded | ByteData or string | ByteData/string which contains the decoded version of source. |

love.data.decode(container, format, sourceData)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the decoded data as. |
| format | EncodeFormat | The format of the input data. |
| sourceData | Data | The raw (encoded) data to decode. |

| name | type | description |
| --- | --- | --- |
| decoded | ByteData or string | ByteData/string which contains the decoded version of source. |


love.data.decompress

Decompresses a CompressedData or previously compressed string or Data object.

love.data.decompress(container, compressedData)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the decompressed data as. |
| compressedData | CompressedData | The compressed data to decompress. |

| name | type | description |
| --- | --- | --- |
| decompressedData | Data or string | Data/string containing the raw decompressed data. |

love.data.decompress(container, format, compressedString)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the decompressed data as. |
| format | CompressedDataFormat | The format that was used to compress the given string. |
| compressedString | string | A string containing data previously compressed with love.data.compress. |

| name | type | description |
| --- | --- | --- |
| decompressedData | Data or string | Data/string containing the raw decompressed data. |

love.data.decompress(container, format, data)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the decompressed data as. |
| format | CompressedDataFormat | The format that was used to compress the given data. |
| data | Data | A Data object containing data previously compressed with love.data.compress. |

| name | type | description |
| --- | --- | --- |
| decompressedData | Data or string | Data/string containing the raw decompressed data. |


love.data.encode

Encode Data or a string to a Data or string in one of the EncodeFormats.

love.data.encode(container, format, sourceString, linelength)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the encoded data as. |
| format | EncodeFormat | The format of the output data. |
| sourceString | string | The raw data to encode. |
| linelength | number | The maximum line length of the output. Only supported for base64, ignored if 0. |

| name | type | description |
| --- | --- | --- |
| encoded | ByteData or string | ByteData/string which contains the encoded version of source. |

love.data.encode(container, format, sourceData, linelength)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the encoded data as. |
| format | EncodeFormat | The format of the output data. |
| sourceData | Data | The raw data to encode. |
| linelength | number | The maximum line length of the output. Only supported for base64, ignored if 0. |

| name | type | description |
| --- | --- | --- |
| encoded | ByteData or string | ByteData/string which contains the encoded version of source. |


love.data.getPackedSize

Gets the size in bytes that a given format used with love.data.pack will use.

This function behaves the same as Lua 5.3's string.packsize.

love.data.getPackedSize(format)

| name | type | description |
| --- | --- | --- |
| format | string | A string determining how the values are packed. Follows the rules of Lua 5.3's string.pack format strings. |

| name | type | description |
| --- | --- | --- |
| size | number | The size in bytes that the packed data will use. |


love.data.hash

Compute the message digest of a string using a specified hash algorithm.

love.data.hash(hashFunction, string)

| name | type | description |
| --- | --- | --- |
| hashFunction | HashFunction | Hash algorithm to use. |
| string | string | String to hash. |

| name | type | description |
| --- | --- | --- |
| rawdigest | string | Raw message digest string. |

love.data.hash(hashFunction, data)

| name | type | description |
| --- | --- | --- |
| hashFunction | HashFunction | Hash algorithm to use. |
| data | Data | Data to hash. |

| name | type | description |
| --- | --- | --- |
| rawdigest | string | Raw message digest string. |


love.data.newByteData

Creates a new Data object containing arbitrary bytes.

Data:getPointer along with LuaJIT's FFI can be used to manipulate the contents of the ByteData object after it has been created.

love.data.newByteData(datastring)

| name | type | description |
| --- | --- | --- |
| datastring | string | The byte string to copy. |

| name | type | description |
| --- | --- | --- |
| bytedata | ByteData | The new Data object. |

love.data.newByteData(Data, offset, size)

| name | type | description |
| --- | --- | --- |
| Data | Data | The existing Data object to copy. |
| offset | number | The offset of the subsection to copy, in bytes. |
| size | number | The size in bytes of the new Data object. |

| name | type | description |
| --- | --- | --- |
| bytedata | ByteData | The new Data object. |

love.data.newByteData(size)

| name | type | description |
| --- | --- | --- |
| size | number | The size in bytes of the new Data object. |

| name | type | description |
| --- | --- | --- |
| bytedata | ByteData | The new Data object. |


love.data.newDataView

Creates a new Data referencing a subsection of an existing Data object.

love.data.newDataView(data, offset, size)

| name | type | description |
| --- | --- | --- |
| data | Data | The Data object to reference. |
| offset | number | The offset of the subsection to reference, in bytes. |
| size | number | The size in bytes of the subsection to reference. |

| name | type | description |
| --- | --- | --- |
| view | Data | The new Data view. |


love.data.pack

Packs (serializes) simple Lua values.

This function behaves the same as Lua 5.3's string.pack.

love.data.pack(container, format, v1, ...)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the encoded data as. |
| format | string | A string determining how the values are packed. Follows the rules of Lua 5.3's string.pack format strings. |
| v1 | number or boolean or string | The first value (number, boolean, or string) to serialize. |
| ... | number or boolean or string | Additional values to serialize. |

| name | type | description |
| --- | --- | --- |
| data | Data or string | Data/string which contains the serialized data. |


love.data.unpack

Unpacks (deserializes) a byte-string or Data into simple Lua values.

This function behaves the same as Lua 5.3's string.unpack.

love.data.unpack(format, datastring, pos)

| name | type | description |
| --- | --- | --- |
| format | string | A string determining how the values were packed. Follows the rules of Lua 5.3's string.pack format strings. |
| datastring | string | A string containing the packed (serialized) data. |
| pos | number | Where to start reading in the string. Negative values can be used to read relative from the end of the string. |

| name | type | description |
| --- | --- | --- |
| v1 | number or boolean or string | The first value (number, boolean, or string) that was unpacked. |
| ... | number or boolean or string | Additional unpacked values. |
| index | number | The index of the first unread byte in the data string. |

love.data.unpack(format, data, pos)

| name | type | description |
| --- | --- | --- |
| format | string | A string determining how the values were packed. Follows the rules of Lua 5.3's string.pack format strings. |
| data | Data | A Data object containing the packed (serialized) data. |
| pos | number | 1-based index indicating where to start reading in the Data. Negative values can be used to read relative from the end of the Data object. |

| name | type | description |
| --- | --- | --- |
| v1 | number or boolean or string | The first value (number, boolean, or string) that was unpacked. |
| ... | number or boolean or string | Additional unpacked values. |
| index | number | The 1-based index of the first unread byte in the Data. |


love.directorydropped

Callback function triggered when a directory is dragged and dropped onto the window.

love.directorydropped(path)

| name | type | description |
| --- | --- | --- |
| path | string | The full platform-dependent path to the directory. It can be used as an argument to love.filesystem.mount, in order to gain read access to the directory with love.filesystem. |


love.displayrotated

Called when the device display orientation changed, for example, user rotated their phone 180 degrees.

love.displayrotated(index, orientation)

| name | type | description |
| --- | --- | --- |
| index | number | The index of the display that changed orientation. |
| orientation | DisplayOrientation | The new orientation. |


love.draw

Callback function used to draw on the screen every frame.

love.draw()


love.errorhandler

The error handler, used to display error messages.

love.errorhandler(msg)

| name | type | description |
| --- | --- | --- |
| msg | string | The error message. |

| name | type | description |
| --- | --- | --- |
| mainLoop | function | Function which handles one frame, including events and rendering, when called. If this is nil then LÖVE exits immediately. |


love.event.clear

Clears the event queue.

love.event.clear()


love.event.poll

Returns an iterator for messages in the event queue.

love.event.poll()

| name | type | description |
| --- | --- | --- |
| i | function | Iterator function usable in a for loop. |


love.event.pump

Pump events into the event queue.

This is a low-level function, and is usually not called by the user, but by love.run.

Note that this does need to be called for any OS to think you're still running,

and if you want to handle OS-generated events at all (think callbacks).

love.event.pump()


love.event.push

Adds an event to the event queue.

From 0.10.0 onwards, you may pass an arbitrary amount of arguments with this function, though the default callbacks don't ever use more than six.

love.event.push(n, a, b, c, d, e, f, ...)

| name | type | description |
| --- | --- | --- |
| n | Event | The name of the event. |
| a | Variant | First event argument. |
| b | Variant | Second event argument. |
| c | Variant | Third event argument. |
| d | Variant | Fourth event argument. |
| e | Variant | Fifth event argument. |
| f | Variant | Sixth event argument. |
| ... | Variant | Further event arguments may follow. |


love.event.quit

Adds the quit event to the queue.

The quit event is a signal for the event handler to close LÖVE. It's possible to abort the exit process with the love.quit callback.

love.event.quit(exitstatus)

| name | type | description |
| --- | --- | --- |
| exitstatus | number | The program exit status to use when closing the application. |

love.event.quit('restart')

| name | type | description |
| --- | --- | --- |
| 'restart' | string | Tells the default love.run to exit and restart the game without relaunching the executable. |


love.event.wait

Like love.event.poll(), but blocks until there is an event in the queue.

love.event.wait()

| name | type | description |
| --- | --- | --- |
| n | Event | The name of event. |
| a | Variant | First event argument. |
| b | Variant | Second event argument. |
| c | Variant | Third event argument. |
| d | Variant | Fourth event argument. |
| e | Variant | Fifth event argument. |
| f | Variant | Sixth event argument. |
| ... | Variant | Further event arguments may follow. |


love.filedropped

Callback function triggered when a file is dragged and dropped onto the window.

love.filedropped(file)

| name | type | description |
| --- | --- | --- |
| file | DroppedFile | The unopened File object representing the file that was dropped. |


love.filesystem.append

Append data to an existing file.

love.filesystem.append(name, data, size)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |
| data | string | The string data to append to the file. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the operation was successful, or nil if there was an error. |
| errormsg | string | The error message on failure. |

love.filesystem.append(name, data, size)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |
| data | Data | The Data object to append to the file. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the operation was successful, or nil if there was an error. |
| errormsg | string | The error message on failure. |


love.filesystem.areSymlinksEnabled

Gets whether love.filesystem follows symbolic links.

love.filesystem.areSymlinksEnabled()

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether love.filesystem follows symbolic links. |


love.filesystem.createDirectory

Recursively creates a directory.

When called with 'a/b' it creates both 'a' and 'a/b', if they don't exist already.

love.filesystem.createDirectory(name)

| name | type | description |
| --- | --- | --- |
| name | string | The directory to create. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the directory was created, false if not. |


love.filesystem.getAppdataDirectory

Returns the application data directory (could be the same as getUserDirectory)

love.filesystem.getAppdataDirectory()

| name | type | description |
| --- | --- | --- |
| path | string | The path of the application data directory |


love.filesystem.getCRequirePath

Gets the filesystem paths that will be searched for c libraries when require is called.

The paths string returned by this function is a sequence of path templates separated by semicolons. The argument passed to ''require'' will be inserted in place of any question mark ('?') character in each template (after the dot characters in the argument passed to ''require'' are replaced by directory separators.) Additionally, any occurrence of a double question mark ('??') will be replaced by the name passed to require and the default library extension for the platform.

The paths are relative to the game's source and save directories, as well as any paths mounted with love.filesystem.mount.

love.filesystem.getCRequirePath()

| name | type | description |
| --- | --- | --- |
| paths | string | The paths that the ''require'' function will check for c libraries in love's filesystem. |


love.filesystem.getDirectoryItems

Returns a table with the names of files and subdirectories in the specified path. The table is not sorted in any way; the order is undefined.

If the path passed to the function exists in the game and the save directory, it will list the files and directories from both places.

love.filesystem.getDirectoryItems(dir)

| name | type | description |
| --- | --- | --- |
| dir | string | The directory. |

| name | type | description |
| --- | --- | --- |
| files | table | A sequence with the names of all files and subdirectories as strings. |

love.filesystem.getDirectoryItems(dir, callback)

| name | type | description |
| --- | --- | --- |
| dir | string | The directory. |
| callback | function | A function which is called for each file and folder in the directory. The filename is passed to the function as an argument. |

| name | type | description |
| --- | --- | --- |
| files | table | A sequence with the names of all files and subdirectories as strings. |


love.filesystem.getIdentity

Gets the write directory name for your game.

Note that this only returns the name of the folder to store your files in, not the full path.

love.filesystem.getIdentity()

| name | type | description |
| --- | --- | --- |
| name | string | The identity that is used as write directory. |


love.filesystem.getInfo

Gets information about the specified file or directory.

love.filesystem.getInfo(path, filtertype)

| name | type | description |
| --- | --- | --- |
| path | string | The file or directory path to check. |
| filtertype | FileType | If supplied, this parameter causes getInfo to only return the info table if the item at the given path matches the specified file type. |

| name | type | description |
| --- | --- | --- |
| info | table | A table containing information about the specified path, or nil if nothing exists at the path. The table contains the following fields: |

love.filesystem.getInfo(path, info)

| name | type | description |
| --- | --- | --- |
| path | string | The file or directory path to check. |
| info | table | A table which will be filled in with info about the specified path. |

| name | type | description |
| --- | --- | --- |
| info | table | The table given as an argument, or nil if nothing exists at the path. The table will be filled in with the following fields: |

love.filesystem.getInfo(path, filtertype, info)

| name | type | description |
| --- | --- | --- |
| path | string | The file or directory path to check. |
| filtertype | FileType | Causes getInfo to only return the info table if the item at the given path matches the specified file type. |
| info | table | A table which will be filled in with info about the specified path. |

| name | type | description |
| --- | --- | --- |
| info | table | The table given as an argument, or nil if nothing exists at the path. The table will be filled in with the following fields: |


love.filesystem.getRealDirectory

Gets the platform-specific absolute path of the directory containing a filepath.

This can be used to determine whether a file is inside the save directory or the game's source .love.

love.filesystem.getRealDirectory(filepath)

| name | type | description |
| --- | --- | --- |
| filepath | string | The filepath to get the directory of. |

| name | type | description |
| --- | --- | --- |
| realdir | string | The platform-specific full path of the directory containing the filepath. |


love.filesystem.getRequirePath

Gets the filesystem paths that will be searched when require is called.

The paths string returned by this function is a sequence of path templates separated by semicolons. The argument passed to ''require'' will be inserted in place of any question mark ('?') character in each template (after the dot characters in the argument passed to ''require'' are replaced by directory separators.)

The paths are relative to the game's source and save directories, as well as any paths mounted with love.filesystem.mount.

love.filesystem.getRequirePath()

| name | type | description |
| --- | --- | --- |
| paths | string | The paths that the ''require'' function will check in love's filesystem. |


love.filesystem.getSaveDirectory

Gets the full path to the designated save directory.

This can be useful if you want to use the standard io library (or something else) to

read or write in the save directory.

love.filesystem.getSaveDirectory()

| name | type | description |
| --- | --- | --- |
| dir | string | The absolute path to the save directory. |


love.filesystem.getSource

Returns the full path to the the .love file or directory. If the game is fused to the LÖVE executable, then the executable is returned.

love.filesystem.getSource()

| name | type | description |
| --- | --- | --- |
| path | string | The full platform-dependent path of the .love file or directory. |


love.filesystem.getSourceBaseDirectory

Returns the full path to the directory containing the .love file. If the game is fused to the LÖVE executable, then the directory containing the executable is returned.

If love.filesystem.isFused is true, the path returned by this function can be passed to love.filesystem.mount, which will make the directory containing the main game (e.g. C:\Program Files\coolgame\) readable by love.filesystem.

love.filesystem.getSourceBaseDirectory()

| name | type | description |
| --- | --- | --- |
| path | string | The full platform-dependent path of the directory containing the .love file. |


love.filesystem.getUserDirectory

Returns the path of the user's directory

love.filesystem.getUserDirectory()

| name | type | description |
| --- | --- | --- |
| path | string | The path of the user's directory |


love.filesystem.getWorkingDirectory

Gets the current working directory.

love.filesystem.getWorkingDirectory()

| name | type | description |
| --- | --- | --- |
| cwd | string | The current working directory. |


love.filesystem.init

Initializes love.filesystem, will be called internally, so should not be used explicitly.

love.filesystem.init(appname)

| name | type | description |
| --- | --- | --- |
| appname | string | The name of the application binary, typically love. |


love.filesystem.isFused

Gets whether the game is in fused mode or not.

If a game is in fused mode, its save directory will be directly in the Appdata directory instead of Appdata/LOVE/. The game will also be able to load C Lua dynamic libraries which are located in the save directory.

A game is in fused mode if the source .love has been fused to the executable (see Game Distribution), or if '--fused' has been given as a command-line argument when starting the game.

love.filesystem.isFused()

| name | type | description |
| --- | --- | --- |
| fused | boolean | True if the game is in fused mode, false otherwise. |


love.filesystem.lines

Iterate over the lines in a file.

love.filesystem.lines(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file |

| name | type | description |
| --- | --- | --- |
| iterator | function | A function that iterates over all the lines in the file |


love.filesystem.load

Loads a Lua file (but does not run it).

love.filesystem.load(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |

| name | type | description |
| --- | --- | --- |
| chunk | function | The loaded chunk. |
| errormsg | string | The error message if file could not be opened. |


love.filesystem.mount

Mounts a zip file or folder in the game's save directory for reading.

It is also possible to mount love.filesystem.getSourceBaseDirectory if the game is in fused mode.

love.filesystem.mount(archive, mountpoint, appendToPath)

| name | type | description |
| --- | --- | --- |
| archive | string | The folder or zip file in the game's save directory to mount. |
| mountpoint | string | The new path the archive will be mounted to. |
| appendToPath | boolean | Whether the archive will be searched when reading a filepath before or after already-mounted archives. This includes the game's source and save directories. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the archive was successfully mounted, false otherwise. |

love.filesystem.mount(filedata, mountpoint, appendToPath)

| name | type | description |
| --- | --- | --- |
| filedata | FileData | The FileData object in memory to mount. |
| mountpoint | string | The new path the archive will be mounted to. |
| appendToPath | boolean | Whether the archive will be searched when reading a filepath before or after already-mounted archives. This includes the game's source and save directories. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the archive was successfully mounted, false otherwise. |

love.filesystem.mount(data, archivename, mountpoint, appendToPath)

| name | type | description |
| --- | --- | --- |
| data | Data | The Data object in memory to mount. |
| archivename | string | The name to associate the mounted data with, for use with love.filesystem.unmount. Must be unique compared to other mounted data. |
| mountpoint | string | The new path the archive will be mounted to. |
| appendToPath | boolean | Whether the archive will be searched when reading a filepath before or after already-mounted archives. This includes the game's source and save directories. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the archive was successfully mounted, false otherwise. |


love.filesystem.newFile

Creates a new File object.

It needs to be opened before it can be accessed.

love.filesystem.newFile(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the file. |

| name | type | description |
| --- | --- | --- |
| file | File | The new File object. |

love.filesystem.newFile(filename, mode)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the file. |
| mode | FileMode | The mode to open the file in. |

| name | type | description |
| --- | --- | --- |
| file | File | The new File object, or nil if an error occurred. |
| errorstr | string | The error string if an error occurred. |


love.filesystem.newFileData

Creates a new FileData object from a file on disk, or from a string in memory.

love.filesystem.newFileData(contents, name)

| name | type | description |
| --- | --- | --- |
| contents | string | The contents of the file in memory represented as a string. |
| name | string | The name of the file. The extension may be parsed and used by LÖVE when passing the FileData object into love.audio.newSource. |

| name | type | description |
| --- | --- | --- |
| data | FileData | The new FileData. |

love.filesystem.newFileData(originaldata, name)

| name | type | description |
| --- | --- | --- |
| originaldata | Data | The Data object to copy into the new FileData object. |
| name | string | The name of the file. The extension may be parsed and used by LÖVE when passing the FileData object into love.audio.newSource. |

| name | type | description |
| --- | --- | --- |
| data | FileData | The new FileData. |

love.filesystem.newFileData(filepath)

| name | type | description |
| --- | --- | --- |
| filepath | string | Path to the file. |

| name | type | description |
| --- | --- | --- |
| data | FileData | The new FileData, or nil if an error occurred. |
| err | string | The error string, if an error occurred. |


love.filesystem.read

Read the contents of a file.

love.filesystem.read(name, size)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |
| size | number | How many bytes to read. |

| name | type | description |
| --- | --- | --- |
| contents | string | The file contents. |
| size | number | How many bytes have been read. |
| contents | nil | returns nil as content. |
| error | string | returns an error message. |

love.filesystem.read(container, name, size)

| name | type | description |
| --- | --- | --- |
| container | ContainerType | What type to return the file's contents as. |
| name | string | The name (and path) of the file |
| size | number | How many bytes to read |

| name | type | description |
| --- | --- | --- |
| contents | FileData or string | FileData or string containing the file contents. |
| size | number | How many bytes have been read. |
| contents | nil | returns nil as content. |
| error | string | returns an error message. |


love.filesystem.remove

Removes a file or empty directory.

love.filesystem.remove(name)

| name | type | description |
| --- | --- | --- |
| name | string | The file or directory to remove. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the file/directory was removed, false otherwise. |


love.filesystem.setCRequirePath

Sets the filesystem paths that will be searched for c libraries when require is called.

The paths string returned by this function is a sequence of path templates separated by semicolons. The argument passed to ''require'' will be inserted in place of any question mark ('?') character in each template (after the dot characters in the argument passed to ''require'' are replaced by directory separators.) Additionally, any occurrence of a double question mark ('??') will be replaced by the name passed to require and the default library extension for the platform.

The paths are relative to the game's source and save directories, as well as any paths mounted with love.filesystem.mount.

love.filesystem.setCRequirePath(paths)

| name | type | description |
| --- | --- | --- |
| paths | string | The paths that the ''require'' function will check in love's filesystem. |


love.filesystem.setIdentity

Sets the write directory for your game.

Note that you can only set the name of the folder to store your files in, not the location.

love.filesystem.setIdentity(name)

| name | type | description |
| --- | --- | --- |
| name | string | The new identity that will be used as write directory. |

love.filesystem.setIdentity(name)

| name | type | description |
| --- | --- | --- |
| name | string | The new identity that will be used as write directory. |


love.filesystem.setRequirePath

Sets the filesystem paths that will be searched when require is called.

The paths string given to this function is a sequence of path templates separated by semicolons. The argument passed to ''require'' will be inserted in place of any question mark ('?') character in each template (after the dot characters in the argument passed to ''require'' are replaced by directory separators.)

The paths are relative to the game's source and save directories, as well as any paths mounted with love.filesystem.mount.

love.filesystem.setRequirePath(paths)

| name | type | description |
| --- | --- | --- |
| paths | string | The paths that the ''require'' function will check in love's filesystem. |


love.filesystem.setSource

Sets the source of the game, where the code is present. This function can only be called once, and is normally automatically done by LÖVE.

love.filesystem.setSource(path)

| name | type | description |
| --- | --- | --- |
| path | string | Absolute path to the game's source folder. |


love.filesystem.setSymlinksEnabled

Sets whether love.filesystem follows symbolic links. It is enabled by default in version 0.10.0 and newer, and disabled by default in 0.9.2.

love.filesystem.setSymlinksEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether love.filesystem should follow symbolic links. |


love.filesystem.unmount

Unmounts a zip file or folder previously mounted for reading with love.filesystem.mount.

love.filesystem.unmount(archive)

| name | type | description |
| --- | --- | --- |
| archive | string | The folder or zip file in the game's save directory which is currently mounted. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if the archive was successfully unmounted, false otherwise. |


love.filesystem.write

Write data to a file in the save directory. If the file existed already, it will be completely replaced by the new contents.

love.filesystem.write(name, data, size)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |
| data | string | The string data to write to the file. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | If the operation was successful. |
| message | string | Error message if operation was unsuccessful. |

love.filesystem.write(name, data, size)

| name | type | description |
| --- | --- | --- |
| name | string | The name (and path) of the file. |
| data | Data | The Data object to write to the file. |
| size | number | How many bytes to write. |

| name | type | description |
| --- | --- | --- |
| success | boolean | If the operation was successful. |
| message | string | Error message if operation was unsuccessful. |


love.focus

Callback function triggered when window receives or loses focus.

love.focus(focus)

| name | type | description |
| --- | --- | --- |
| focus | boolean | True if the window gains focus, false if it loses focus. |


love.font.newBMFontRasterizer

Creates a new BMFont Rasterizer.

love.font.newBMFontRasterizer(imageData, glyphs, dpiscale)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The image data containing the drawable pictures of font glyphs. |
| glyphs | string | The sequence of glyphs in the ImageData. |
| dpiscale | number | DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newBMFontRasterizer(fileName, glyphs, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileName | string | The path to file containing the drawable pictures of font glyphs. |
| glyphs | string | The sequence of glyphs in the ImageData. |
| dpiscale | number | DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |


love.font.newGlyphData

Creates a new GlyphData.

love.font.newGlyphData(rasterizer, glyph)

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The Rasterizer containing the font. |
| glyph | number | The character code of the glyph. |


love.font.newImageRasterizer

Creates a new Image Rasterizer.

love.font.newImageRasterizer(imageData, glyphs, extraSpacing, dpiscale)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | Font image data. |
| glyphs | string | String containing font glyphs. |
| extraSpacing | number | Font extra spacing. |
| dpiscale | number | Font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |


love.font.newRasterizer

Creates a new Rasterizer.

love.font.newRasterizer(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The font file. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(data)

| name | type | description |
| --- | --- | --- |
| data | FileData | The FileData of the font file. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(fileName, size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileName | string | Path to font file. |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(fileData, size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | File data containing font. |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(imageData, glyphs, dpiscale)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The image data containing the drawable pictures of font glyphs. |
| glyphs | string | The sequence of glyphs in the ImageData. |
| dpiscale | number | DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newRasterizer(fileName, glyphs, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileName | string | The path to file containing the drawable pictures of font glyphs. |
| glyphs | string | The sequence of glyphs in the ImageData. |
| dpiscale | number | DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |


love.font.newTrueTypeRasterizer

Creates a new TrueType Rasterizer.

love.font.newTrueTypeRasterizer(size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newTrueTypeRasterizer(fileName, size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileName | string | Path to font file. |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |

love.font.newTrueTypeRasterizer(fileData, size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | File data containing font. |
| size | number | The font size. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The font DPI scale. |

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | The rasterizer. |


love.gamepadaxis

Called when a Joystick's virtual gamepad axis is moved.

love.gamepadaxis(joystick, axis, value)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| axis | GamepadAxis | The virtual gamepad axis. |
| value | number | The new axis value. |


love.gamepadpressed

Called when a Joystick's virtual gamepad button is pressed.

love.gamepadpressed(joystick, button)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| button | GamepadButton | The virtual gamepad button. |


love.gamepadreleased

Called when a Joystick's virtual gamepad button is released.

love.gamepadreleased(joystick, button)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| button | GamepadButton | The virtual gamepad button. |


love.getVersion

Gets the current running version of LÖVE.

love.getVersion()

| name | type | description |
| --- | --- | --- |
| major | number | The major version of LÖVE, i.e. 0 for version 0.9.1. |
| minor | number | The minor version of LÖVE, i.e. 9 for version 0.9.1. |
| revision | number | The revision version of LÖVE, i.e. 1 for version 0.9.1. |
| codename | string | The codename of the current version, i.e. 'Baby Inspector' for version 0.9.1. |


love.graphics.applyTransform

Applies the given Transform object to the current coordinate transformation.

This effectively multiplies the existing coordinate transformation's matrix with the Transform object's internal matrix to produce the new coordinate transformation.

love.graphics.applyTransform(transform)

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object to apply to the current graphics coordinate transform. |


love.graphics.arc

Draws a filled or unfilled arc at position (x, y). The arc is drawn from angle1 to angle2 in radians. The segments parameter determines how many segments are used to draw the arc. The more segments, the smoother the edge.

love.graphics.arc(drawmode, x, y, radius, angle1, angle2, segments)

| name | type | description |
| --- | --- | --- |
| drawmode | DrawMode | How to draw the arc. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radius | number | Radius of the arc. |
| angle1 | number | The angle at which the arc begins. |
| angle2 | number | The angle at which the arc terminates. |
| segments | number | The number of segments used for drawing the arc. |

love.graphics.arc(drawmode, arctype, x, y, radius, angle1, angle2, segments)

| name | type | description |
| --- | --- | --- |
| drawmode | DrawMode | How to draw the arc. |
| arctype | ArcType | The type of arc to draw. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radius | number | Radius of the arc. |
| angle1 | number | The angle at which the arc begins. |
| angle2 | number | The angle at which the arc terminates. |
| segments | number | The number of segments used for drawing the arc. |


love.graphics.captureScreenshot

Creates a screenshot once the current frame is done (after love.draw has finished).

Since this function enqueues a screenshot capture rather than executing it immediately, it can be called from an input callback or love.update and it will still capture all of what's drawn to the screen in that frame.

love.graphics.captureScreenshot(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename to save the screenshot to. The encoded image type is determined based on the extension of the filename, and must be one of the ImageFormats. |

love.graphics.captureScreenshot(callback)

| name | type | description |
| --- | --- | --- |
| callback | function | Function which gets called once the screenshot has been captured. An ImageData is passed into the function as its only argument. |

love.graphics.captureScreenshot(channel)

| name | type | description |
| --- | --- | --- |
| channel | Channel | The Channel to push the generated ImageData to. |


love.graphics.circle

Draws a circle.

love.graphics.circle(mode, x, y, radius)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the circle. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radius | number | The radius of the circle. |

love.graphics.circle(mode, x, y, radius, segments)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the circle. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radius | number | The radius of the circle. |
| segments | number | The number of segments used for drawing the circle. Note: The default variable for the segments parameter varies between different versions of LÖVE. |


love.graphics.clear

Clears the screen or active Canvas to the specified color.

This function is called automatically before love.draw in the default love.run function. See the example in love.run for a typical use of this function.

Note that the scissor area bounds the cleared region.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

In versions prior to background color instead.

love.graphics.clear()

love.graphics.clear(r, g, b, a, clearstencil, cleardepth)

| name | type | description |
| --- | --- | --- |
| r | number | The red channel of the color to clear the screen to. |
| g | number | The green channel of the color to clear the screen to. |
| b | number | The blue channel of the color to clear the screen to. |
| a | number | The alpha channel of the color to clear the screen to. |
| clearstencil | boolean | Whether to clear the active stencil buffer, if present. It can also be an integer between 0 and 255 to clear the stencil buffer to a specific value. |
| cleardepth | boolean | Whether to clear the active depth buffer, if present. It can also be a number between 0 and 1 to clear the depth buffer to a specific value. |

love.graphics.clear(color, ..., clearstencil, cleardepth)

| name | type | description |
| --- | --- | --- |
| color | table | A table in the form of {r, g, b, a} containing the color to clear the first active Canvas to. |
| ... | table | Additional tables for each active Canvas. |
| clearstencil | boolean | Whether to clear the active stencil buffer, if present. It can also be an integer between 0 and 255 to clear the stencil buffer to a specific value. |
| cleardepth | boolean | Whether to clear the active depth buffer, if present. It can also be a number between 0 and 1 to clear the depth buffer to a specific value. |

love.graphics.clear(clearcolor, clearstencil, cleardepth)

| name | type | description |
| --- | --- | --- |
| clearcolor | boolean | Whether to clear the active color canvas to transparent black (0, 0, 0, 0). Typically this should be set to false with this variant of the function. |
| clearstencil | boolean | Whether to clear the active stencil buffer, if present. It can also be an integer between 0 and 255 to clear the stencil buffer to a specific value. |
| cleardepth | boolean | Whether to clear the active depth buffer, if present. It can also be a number between 0 and 1 to clear the depth buffer to a specific value. |


love.graphics.discard

Discards (trashes) the contents of the screen or active Canvas. This is a performance optimization function with niche use cases.

If the active Canvas has just been changed and the 'replace' BlendMode is about to be used to draw something which covers the entire screen, calling love.graphics.discard rather than calling love.graphics.clear or doing nothing may improve performance on mobile devices.

On some desktop systems this function may do nothing.

love.graphics.discard(discardcolor, discardstencil)

| name | type | description |
| --- | --- | --- |
| discardcolor | boolean | Whether to discard the texture(s) of the active Canvas(es) (the contents of the screen if no Canvas is active.) |
| discardstencil | boolean | Whether to discard the contents of the stencil buffer of the screen / active Canvas. |

love.graphics.discard(discardcolors, discardstencil)

| name | type | description |
| --- | --- | --- |
| discardcolors | table | An array containing boolean values indicating whether to discard the texture of each active Canvas, when multiple simultaneous Canvases are active. |
| discardstencil | boolean | Whether to discard the contents of the stencil buffer of the screen / active Canvas. |


love.graphics.draw

Draws a Drawable object (an Image, Canvas, SpriteBatch, ParticleSystem, Mesh, Text object, or Video) on the screen with optional rotation, scaling and shearing.

Objects are drawn relative to their local coordinate system. The origin is by default located at the top left corner of Image and Canvas. All scaling, shearing, and rotation arguments transform the object relative to that point. Also, the position of the origin can be specified on the screen coordinate system.

It's possible to rotate an object about its center by offsetting the origin to the center. Angles must be given in radians for rotation. One can also use a negative scaling factor to flip about its centerline.

Note that the offsets are applied before rotation, scaling, or shearing; scaling and shearing are applied before rotation.

The right and bottom edges of the object are shifted at an angle defined by the shearing factors.

When using the default shader anything drawn with this function will be tinted according to the currently selected color.  Set it to pure white to preserve the object's original colors.

love.graphics.draw(drawable, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| drawable | Drawable | A drawable object. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.draw(texture, quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| texture | Texture | A Texture (Image or Canvas) to texture the Quad with. |
| quad | Quad | The Quad to draw on screen. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.draw(drawable, transform)

| name | type | description |
| --- | --- | --- |
| drawable | Drawable | A drawable object. |
| transform | Transform | Transformation object. |

love.graphics.draw(texture, quad, transform)

| name | type | description |
| --- | --- | --- |
| texture | Texture | A Texture (Image or Canvas) to texture the Quad with. |
| quad | Quad | The Quad to draw on screen. |
| transform | Transform | Transformation object. |


love.graphics.drawInstanced

Draws many instances of a Mesh with a single draw call, using hardware geometry instancing.

Each instance can have unique properties (positions, colors, etc.) but will not by default unless a custom per-instance vertex attributes or the love_InstanceID GLSL 3 vertex shader variable is used, otherwise they will all render at the same position on top of each other.

Instancing is not supported by some older GPUs that are only capable of using OpenGL ES 2 or OpenGL 2. Use love.graphics.getSupported to check.

love.graphics.drawInstanced(mesh, instancecount, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The mesh to render. |
| instancecount | number | The number of instances to render. |
| x | number | The position to draw the instances (x-axis). |
| y | number | The position to draw the instances (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.drawInstanced(mesh, instancecount, transform)

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The mesh to render. |
| instancecount | number | The number of instances to render. |
| transform | Transform | A transform object. |


love.graphics.drawLayer

Draws a layer of an Array Texture.

love.graphics.drawLayer(texture, layerindex, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Array Texture to draw. |
| layerindex | number | The index of the layer to use when drawing. |
| x | number | The position to draw the texture (x-axis). |
| y | number | The position to draw the texture (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.drawLayer(texture, layerindex, quad, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Array Texture to draw. |
| layerindex | number | The index of the layer to use when drawing. |
| quad | Quad | The subsection of the texture's layer to use when drawing. |
| x | number | The position to draw the texture (x-axis). |
| y | number | The position to draw the texture (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.drawLayer(texture, layerindex, transform)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Array Texture to draw. |
| layerindex | number | The index of the layer to use when drawing. |
| transform | Transform | A transform object. |

love.graphics.drawLayer(texture, layerindex, quad, transform)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Array Texture to draw. |
| layerindex | number | The index of the layer to use when drawing. |
| quad | Quad | The subsection of the texture's layer to use when drawing. |
| transform | Transform | A transform object. |


love.graphics.ellipse

Draws an ellipse.

love.graphics.ellipse(mode, x, y, radiusx, radiusy)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the ellipse. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radiusx | number | The radius of the ellipse along the x-axis (half the ellipse's width). |
| radiusy | number | The radius of the ellipse along the y-axis (half the ellipse's height). |

love.graphics.ellipse(mode, x, y, radiusx, radiusy, segments)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the ellipse. |
| x | number | The position of the center along x-axis. |
| y | number | The position of the center along y-axis. |
| radiusx | number | The radius of the ellipse along the x-axis (half the ellipse's width). |
| radiusy | number | The radius of the ellipse along the y-axis (half the ellipse's height). |
| segments | number | The number of segments used for drawing the ellipse. |


love.graphics.flushBatch

Immediately renders any pending automatically batched draws.

LÖVE will call this function internally as needed when most state is changed, so it is not necessary to manually call it.

The current batch will be automatically flushed by love.graphics state changes (except for the transform stack and the current color), as well as Shader:send and methods on Textures which change their state. Using a different Image in consecutive love.graphics.draw calls will also flush the current batch.

SpriteBatches, ParticleSystems, Meshes, and Text objects do their own batching and do not affect automatic batching of other draws, aside from flushing the current batch when they're drawn.

love.graphics.flushBatch()


love.graphics.getBackgroundColor

Gets the current background color.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.getBackgroundColor()

| name | type | description |
| --- | --- | --- |
| r | number | The red component (0-1). |
| g | number | The green component (0-1). |
| b | number | The blue component (0-1). |
| a | number | The alpha component (0-1). |


love.graphics.getBlendMode

Gets the blending mode.

love.graphics.getBlendMode()

| name | type | description |
| --- | --- | --- |
| mode | BlendMode | The current blend mode. |
| alphamode | BlendAlphaMode | The current blend alpha mode – it determines how the alpha of drawn objects affects blending. |


love.graphics.getCanvas

Gets the current target Canvas.

love.graphics.getCanvas()

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | The Canvas set by setCanvas. Returns nil if drawing to the real screen. |


love.graphics.getCanvasFormats

Gets the available Canvas formats, and whether each is supported.

love.graphics.getCanvasFormats()

| name | type | description |
| --- | --- | --- |
| formats | table | A table containing CanvasFormats as keys, and a boolean indicating whether the format is supported as values. Not all systems support all formats. |

love.graphics.getCanvasFormats(readable)

| name | type | description |
| --- | --- | --- |
| readable | boolean | If true, the returned formats will only be indicated as supported if readable flag set to true for that format, and vice versa if the parameter is false. |

| name | type | description |
| --- | --- | --- |
| formats | table | A table containing CanvasFormats as keys, and a boolean indicating whether the format is supported as values (taking into account the readable parameter). Not all systems support all formats. |


love.graphics.getColor

Gets the current color.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.getColor()

| name | type | description |
| --- | --- | --- |
| r | number | The red component (0-1). |
| g | number | The green component (0-1). |
| b | number | The blue component (0-1). |
| a | number | The alpha component (0-1). |


love.graphics.getColorMask

Gets the active color components used when drawing. Normally all 4 components are active unless love.graphics.setColorMask has been used.

The color mask determines whether individual components of the colors of drawn objects will affect the color of the screen. They affect love.graphics.clear and Canvas:clear as well.

love.graphics.getColorMask()

| name | type | description |
| --- | --- | --- |
| r | boolean | Whether the red color component is active when rendering. |
| g | boolean | Whether the green color component is active when rendering. |
| b | boolean | Whether the blue color component is active when rendering. |
| a | boolean | Whether the alpha color component is active when rendering. |


love.graphics.getDPIScale

Gets the DPI scale factor of the window.

The DPI scale factor represents relative pixel density. The pixel density inside the window might be greater (or smaller) than the 'size' of the window. For example on a retina screen in Mac OS X with the highdpi window flag enabled, the window may take up the same physical size as an 800x600 window, but the area inside the window uses 1600x1200 pixels. love.graphics.getDPIScale() would return 2 in that case.

The love.window.fromPixels and love.window.toPixels functions can also be used to convert between units.

The highdpi window flag must be enabled to use the full pixel density of a Retina screen on Mac OS X and iOS. The flag currently does nothing on Windows and Linux, and on Android it is effectively always enabled.

love.graphics.getDPIScale()

| name | type | description |
| --- | --- | --- |
| scale | number | The pixel scale factor associated with the window. |


love.graphics.getDefaultFilter

Returns the default scaling filters used with Images, Canvases, and Fonts.

love.graphics.getDefaultFilter()

| name | type | description |
| --- | --- | --- |
| min | FilterMode | Filter mode used when scaling the image down. |
| mag | FilterMode | Filter mode used when scaling the image up. |
| anisotropy | number | Maximum amount of Anisotropic Filtering used. |


love.graphics.getDepthMode

Gets the current depth test mode and whether writing to the depth buffer is enabled.

This is low-level functionality designed for use with custom vertex shaders and Meshes with custom vertex attributes. No higher level APIs are provided to set the depth of 2D graphics such as shapes, lines, and Images.

love.graphics.getDepthMode()

| name | type | description |
| --- | --- | --- |
| comparemode | CompareMode | Depth comparison mode used for depth testing. |
| write | boolean | Whether to write update / write values to the depth buffer when rendering. |


love.graphics.getDimensions

Gets the width and height in pixels of the window.

love.graphics.getDimensions()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the window. |
| height | number | The height of the window. |


love.graphics.getFont

Gets the current Font object.

love.graphics.getFont()

| name | type | description |
| --- | --- | --- |
| font | Font | The current Font. Automatically creates and sets the default font, if none is set yet. |


love.graphics.getFrontFaceWinding

Gets whether triangles with clockwise- or counterclockwise-ordered vertices are considered front-facing.

This is designed for use in combination with Mesh face culling. Other love.graphics shapes, lines, and sprites are not guaranteed to have a specific winding order to their internal vertices.

love.graphics.getFrontFaceWinding()

| name | type | description |
| --- | --- | --- |
| winding | VertexWinding | The winding mode being used. The default winding is counterclockwise ('ccw'). |


love.graphics.getHeight

Gets the height in pixels of the window.

love.graphics.getHeight()

| name | type | description |
| --- | --- | --- |
| height | number | The height of the window. |


love.graphics.getImageFormats

Gets the raw and compressed pixel formats usable for Images, and whether each is supported.

love.graphics.getImageFormats()

| name | type | description |
| --- | --- | --- |
| formats | table | A table containing PixelFormats as keys, and a boolean indicating whether the format is supported as values. Not all systems support all formats. |


love.graphics.getLineJoin

Gets the line join style.

love.graphics.getLineJoin()

| name | type | description |
| --- | --- | --- |
| join | LineJoin | The LineJoin style. |


love.graphics.getLineStyle

Gets the line style.

love.graphics.getLineStyle()

| name | type | description |
| --- | --- | --- |
| style | LineStyle | The current line style. |


love.graphics.getLineWidth

Gets the current line width.

love.graphics.getLineWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The current line width. |


love.graphics.getMeshCullMode

Gets whether back-facing triangles in a Mesh are culled.

Mesh face culling is designed for use with low level custom hardware-accelerated 3D rendering via custom vertex attributes on Meshes, custom vertex shaders, and depth testing with a depth buffer.

love.graphics.getMeshCullMode()

| name | type | description |
| --- | --- | --- |
| mode | CullMode | The Mesh face culling mode in use (whether to render everything, cull back-facing triangles, or cull front-facing triangles). |


love.graphics.getPixelDimensions

Gets the width and height in pixels of the window.

love.graphics.getDimensions gets the dimensions of the window in units scaled by the screen's DPI scale factor, rather than pixels. Use getDimensions for calculations related to drawing to the screen and using the graphics coordinate system (calculating the center of the screen, for example), and getPixelDimensions only when dealing specifically with underlying pixels (pixel-related calculations in a pixel Shader, for example).

love.graphics.getPixelDimensions()

| name | type | description |
| --- | --- | --- |
| pixelwidth | number | The width of the window in pixels. |
| pixelheight | number | The height of the window in pixels. |


love.graphics.getPixelHeight

Gets the height in pixels of the window.

The graphics coordinate system and DPI scale factor, rather than raw pixels. Use getHeight for calculations related to drawing to the screen and using the coordinate system (calculating the center of the screen, for example), and getPixelHeight only when dealing specifically with underlying pixels (pixel-related calculations in a pixel Shader, for example).

love.graphics.getPixelHeight()

| name | type | description |
| --- | --- | --- |
| pixelheight | number | The height of the window in pixels. |


love.graphics.getPixelWidth

Gets the width in pixels of the window.

The graphics coordinate system and DPI scale factor, rather than raw pixels. Use getWidth for calculations related to drawing to the screen and using the coordinate system (calculating the center of the screen, for example), and getPixelWidth only when dealing specifically with underlying pixels (pixel-related calculations in a pixel Shader, for example).

love.graphics.getPixelWidth()

| name | type | description |
| --- | --- | --- |
| pixelwidth | number | The width of the window in pixels. |


love.graphics.getPointSize

Gets the point size.

love.graphics.getPointSize()

| name | type | description |
| --- | --- | --- |
| size | number | The current point size. |


love.graphics.getRendererInfo

Gets information about the system's video card and drivers.

love.graphics.getRendererInfo()

| name | type | description |
| --- | --- | --- |
| name | string | The name of the renderer, e.g. 'OpenGL' or 'OpenGL ES'. |
| version | string | The version of the renderer with some extra driver-dependent version info, e.g. '2.1 INTEL-8.10.44'. |
| vendor | string | The name of the graphics card vendor, e.g. 'Intel Inc'. |
| device | string | The name of the graphics card, e.g. 'Intel HD Graphics 3000 OpenGL Engine'. |


love.graphics.getScissor

Gets the current scissor box.

love.graphics.getScissor()

| name | type | description |
| --- | --- | --- |
| x | number | The x-component of the top-left point of the box. |
| y | number | The y-component of the top-left point of the box. |
| width | number | The width of the box. |
| height | number | The height of the box. |


love.graphics.getShader

Gets the current Shader. Returns nil if none is set.

love.graphics.getShader()

| name | type | description |
| --- | --- | --- |
| shader | Shader | The currently active Shader, or nil if none is set. |


love.graphics.getStackDepth

Gets the current depth of the transform / state stack (the number of pushes without corresponding pops).

love.graphics.getStackDepth()

| name | type | description |
| --- | --- | --- |
| depth | number | The current depth of the transform and state love.graphics stack. |


love.graphics.getStats

Gets performance-related rendering statistics.

love.graphics.getStats()

| name | type | description |
| --- | --- | --- |
| stats | table | A table with the following fields: |

love.graphics.getStats(stats)

| name | type | description |
| --- | --- | --- |
| stats | table | A table which will be filled in with the stat fields below. |

| name | type | description |
| --- | --- | --- |
| stats | table | The table that was passed in above, now containing the following fields: |


love.graphics.getStencilTest

Gets the current stencil test configuration.

When stencil testing is enabled, the geometry of everything that is drawn afterward will be clipped / stencilled out based on a comparison between the arguments of this function and the stencil value of each pixel that the geometry touches. The stencil values of pixels are affected via love.graphics.stencil.

Each Canvas has its own per-pixel stencil values.

love.graphics.getStencilTest()

| name | type | description |
| --- | --- | --- |
| comparemode | CompareMode | The type of comparison that is made for each pixel. Will be 'always' if stencil testing is disabled. |
| comparevalue | number | The value used when comparing with the stencil value of each pixel. |


love.graphics.getSupported

Gets the optional graphics features and whether they're supported on the system.

Some older or low-end systems don't always support all graphics features.

love.graphics.getSupported()

| name | type | description |
| --- | --- | --- |
| features | table | A table containing GraphicsFeature keys, and boolean values indicating whether each feature is supported. |


love.graphics.getSystemLimits

Gets the system-dependent maximum values for love.graphics features.

love.graphics.getSystemLimits()

| name | type | description |
| --- | --- | --- |
| limits | table | A table containing GraphicsLimit keys, and number values. |


love.graphics.getTextureTypes

Gets the available texture types, and whether each is supported.

love.graphics.getTextureTypes()

| name | type | description |
| --- | --- | --- |
| texturetypes | table | A table containing TextureTypes as keys, and a boolean indicating whether the type is supported as values. Not all systems support all types. |


love.graphics.getWidth

Gets the width in pixels of the window.

love.graphics.getWidth()

| name | type | description |
| --- | --- | --- |
| width | number | The width of the window. |


love.graphics.intersectScissor

Sets the scissor to the rectangle created by the intersection of the specified rectangle with the existing scissor.  If no scissor is active yet, it behaves like love.graphics.setScissor.

The scissor limits the drawing area to a specified rectangle. This affects all graphics calls, including love.graphics.clear.

The dimensions of the scissor is unaffected by graphical transformations (translate, scale, ...).

love.graphics.intersectScissor(x, y, width, height)

| name | type | description |
| --- | --- | --- |
| x | number | The x-coordinate of the upper left corner of the rectangle to intersect with the existing scissor rectangle. |
| y | number | The y-coordinate of the upper left corner of the rectangle to intersect with the existing scissor rectangle. |
| width | number | The width of the rectangle to intersect with the existing scissor rectangle. |
| height | number | The height of the rectangle to intersect with the existing scissor rectangle. |


love.graphics.inverseTransformPoint

Converts the given 2D position from screen-space into global coordinates.

This effectively applies the reverse of the current graphics transformations to the given position. A similar Transform:inverseTransformPoint method exists for Transform objects.

love.graphics.inverseTransformPoint(screenX, screenY)

| name | type | description |
| --- | --- | --- |
| screenX | number | The x component of the screen-space position. |
| screenY | number | The y component of the screen-space position. |

| name | type | description |
| --- | --- | --- |
| globalX | number | The x component of the position in global coordinates. |
| globalY | number | The y component of the position in global coordinates. |


love.graphics.isActive

Gets whether the graphics module is able to be used. If it is not active, love.graphics function and method calls will not work correctly and may cause the program to crash.
The graphics module is inactive if a window is not open, or if the app is in the background on iOS. Typically the app's execution will be automatically paused by the system, in the latter case.

love.graphics.isActive()

| name | type | description |
| --- | --- | --- |
| active | boolean | Whether the graphics module is active and able to be used. |


love.graphics.isGammaCorrect

Gets whether gamma-correct rendering is supported and enabled. It can be enabled by setting t.gammacorrect = true in love.conf.

Not all devices support gamma-correct rendering, in which case it will be automatically disabled and this function will return false. It is supported on desktop systems which have graphics cards that are capable of using OpenGL 3 / DirectX 10, and iOS devices that can use OpenGL ES 3.

love.graphics.isGammaCorrect()

| name | type | description |
| --- | --- | --- |
| gammacorrect | boolean | True if gamma-correct rendering is supported and was enabled in love.conf, false otherwise. |


love.graphics.isWireframe

Gets whether wireframe mode is used when drawing.

love.graphics.isWireframe()

| name | type | description |
| --- | --- | --- |
| wireframe | boolean | True if wireframe lines are used when drawing, false if it's not. |


love.graphics.line

Draws lines between points.

love.graphics.line(x1, y1, x2, y2, ...)

| name | type | description |
| --- | --- | --- |
| x1 | number | The position of first point on the x-axis. |
| y1 | number | The position of first point on the y-axis. |
| x2 | number | The position of second point on the x-axis. |
| y2 | number | The position of second point on the y-axis. |
| ... | number | You can continue passing point positions to draw a polyline. |

love.graphics.line(points)

| name | type | description |
| --- | --- | --- |
| points | table | A table of point positions, as described above. |


love.graphics.newArrayImage

Creates a new array Image.

An array image / array texture is a single object which contains multiple 'layers' or 'slices' of 2D sub-images. It can be thought of similarly to a texture atlas or sprite sheet, but it doesn't suffer from the same tile / quad bleeding artifacts that texture atlases do – although every sub-image must have the same dimensions.

A specific layer of an array image can be drawn with love.graphics.drawLayer / SpriteBatch:addLayer, or with the Quad variant of love.graphics.draw and Quad:setLayer, or via a custom Shader.

To use an array image in a Shader, it must be declared as a ArrayImage or sampler2DArray type (instead of Image or sampler2D). The Texel(ArrayImage image, vec3 texturecoord) shader function must be used to get pixel colors from a slice of the array image. The vec3 argument contains the texture coordinate in the first two components, and the 0-based slice index in the third component.

love.graphics.newArrayImage(slices, settings)

| name | type | description |
| --- | --- | --- |
| slices | table | A table containing filepaths to images (or File, FileData, ImageData, or CompressedImageData objects), in an array. Each sub-image must have the same dimensions. A table of tables can also be given, where each sub-table contains all mipmap levels for the slice index of that sub-table. |
| settings | table | Optional table of settings to configure the array image, containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | An Array Image object. |


love.graphics.newCanvas

Creates a new Canvas object for offscreen rendering.

love.graphics.newCanvas()

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | A new Canvas with dimensions equal to the window's size in pixels. |

love.graphics.newCanvas(width, height)

| name | type | description |
| --- | --- | --- |
| width | number | The desired width of the Canvas. |
| height | number | The desired height of the Canvas. |

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | A new Canvas with specified width and height. |

love.graphics.newCanvas(width, height, settings)

| name | type | description |
| --- | --- | --- |
| width | number | The desired width of the Canvas. |
| height | number | The desired height of the Canvas. |
| settings | table | A table containing the given fields: |

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | A new Canvas with specified width and height. |

love.graphics.newCanvas(width, height, layers, settings)

| name | type | description |
| --- | --- | --- |
| width | number | The desired width of the Canvas. |
| height | number | The desired height of the Canvas. |
| layers | number | The number of array layers (if the Canvas is an Array Texture), or the volume depth (if the Canvas is a Volume Texture). |
| settings | table | A table containing the given fields: |

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | A new Canvas with specified width and height. |


love.graphics.newCubeImage

Creates a new cubemap Image.

Cubemap images have 6 faces (sides) which represent a cube. They can't be rendered directly, they can only be used in Shader code (and sent to the shader via Shader:send).

To use a cubemap image in a Shader, it must be declared as a CubeImage or samplerCube type (instead of Image or sampler2D). The Texel(CubeImage image, vec3 direction) shader function must be used to get pixel colors from the cubemap. The vec3 argument is a normalized direction from the center of the cube, rather than explicit texture coordinates.

Each face in a cubemap image must have square dimensions.

For variants of this function which accept a single image containing multiple cubemap faces, they must be laid out in one of the following forms in the image:

   +y

+z +x -z

   -y

   -x

or:

   +y

-x +z +x -z

   -y

or:

+x

-x

+y

-y

+z

-z

or:

+x -x +y -y +z -z

love.graphics.newCubeImage(filename, settings)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to a cubemap image file (or a File, FileData, or ImageData). |
| settings | table | Optional table of settings to configure the cubemap image, containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | An cubemap Image object. |

love.graphics.newCubeImage(faces, settings)

| name | type | description |
| --- | --- | --- |
| faces | table | A table containing 6 filepaths to images (or File, FileData, ImageData, or CompressedImageData objects), in an array. Each face image must have the same dimensions. A table of tables can also be given, where each sub-table contains all mipmap levels for the cube face index of that sub-table. |
| settings | table | Optional table of settings to configure the cubemap image, containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | An cubemap Image object. |


love.graphics.newFont

Creates a new Font from a TrueType Font or BMFont file. Created fonts are not cached, in that calling this function with the same arguments will always create a new Font object.

All variants which accept a filename can also accept a Data object instead.

love.graphics.newFont(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the BMFont or TrueType font file. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |

love.graphics.newFont(filename, size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the TrueType font file. |
| size | number | The size of the font in pixels. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The DPI scale factor of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |

love.graphics.newFont(filename, imagefilename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the BMFont file. |
| imagefilename | string | The filepath to the BMFont's image file. If this argument is omitted, the path specified inside the BMFont file will be used. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |

love.graphics.newFont(size, hinting, dpiscale)

| name | type | description |
| --- | --- | --- |
| size | number | The size of the font in pixels. |
| hinting | HintingMode | True Type hinting mode. |
| dpiscale | number | The DPI scale factor of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |


love.graphics.newImage

Creates a new Image from a filepath, FileData, an ImageData, or a CompressedImageData, and optionally generates or specifies mipmaps for the image.

love.graphics.newImage(filename, settings)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the image file. |
| settings | table | A table containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | A new Image object which can be drawn on screen. |

love.graphics.newImage(fileData, settings)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | The FileData containing image file. |
| settings | table | A table containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | A new Image object which can be drawn on screen. |

love.graphics.newImage(imageData, settings)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The ImageData containing image. |
| settings | table | A table containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | A new Image object which can be drawn on screen. |

love.graphics.newImage(compressedImageData, settings)

| name | type | description |
| --- | --- | --- |
| compressedImageData | CompressedImageData | A CompressedImageData object. The Image will use this CompressedImageData to reload itself when love.window.setMode is called. |
| settings | table | A table containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | A new Image object which can be drawn on screen. |


love.graphics.newImageFont

Creates a new specifically formatted image.

In versions prior to 0.9.0, LÖVE expects ISO 8859-1 encoding for the glyphs string.

love.graphics.newImageFont(filename, glyphs)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the image file. |
| glyphs | string | A string of the characters in the image in order from left to right. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |

love.graphics.newImageFont(imageData, glyphs)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The ImageData object to create the font from. |
| glyphs | string | A string of the characters in the image in order from left to right. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |

love.graphics.newImageFont(filename, glyphs, extraspacing)

| name | type | description |
| --- | --- | --- |
| filename | string | The filepath to the image file. |
| glyphs | string | A string of the characters in the image in order from left to right. |
| extraspacing | number | Additional spacing (positive or negative) to apply to each glyph in the Font. |

| name | type | description |
| --- | --- | --- |
| font | Font | A Font object which can be used to draw text on screen. |


love.graphics.newMesh

Creates a new Mesh.

Use Mesh:setTexture if the Mesh should be textured with an Image or Canvas when it's drawn.

In versions prior to 11.0, color and byte component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.newMesh(vertices, mode, usage)

| name | type | description |
| --- | --- | --- |
| vertices | table | The table filled with vertex information tables for each vertex as follows: |
| mode | MeshDrawMode | How the vertices are used when drawing. The default mode 'fan' is sufficient for simple convex polygons. |
| usage | SpriteBatchUsage | The expected usage of the Mesh. The specified usage mode affects the Mesh's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The new mesh. |

love.graphics.newMesh(vertexcount, mode, usage)

| name | type | description |
| --- | --- | --- |
| vertexcount | number | The total number of vertices the Mesh will use. Each vertex is initialized to {0,0, 0,0, 1,1,1,1}. |
| mode | MeshDrawMode | How the vertices are used when drawing. The default mode 'fan' is sufficient for simple convex polygons. |
| usage | SpriteBatchUsage | The expected usage of the Mesh. The specified usage mode affects the Mesh's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The new mesh. |

love.graphics.newMesh(vertexformat, vertices, mode, usage)

| name | type | description |
| --- | --- | --- |
| vertexformat | table | A table in the form of {attribute, ...}. Each attribute is a table which specifies a custom vertex attribute used for each vertex. |
| vertices | table | The table filled with vertex information tables for each vertex, in the form of {vertex, ...} where each vertex is a table in the form of {attributecomponent, ...}. |
| mode | MeshDrawMode | How the vertices are used when drawing. The default mode 'fan' is sufficient for simple convex polygons. |
| usage | SpriteBatchUsage | The expected usage of the Mesh. The specified usage mode affects the Mesh's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The new mesh. |

love.graphics.newMesh(vertexformat, vertexcount, mode, usage)

| name | type | description |
| --- | --- | --- |
| vertexformat | table | A table in the form of {attribute, ...}. Each attribute is a table which specifies a custom vertex attribute used for each vertex. |
| vertexcount | number | The total number of vertices the Mesh will use. |
| mode | MeshDrawMode | How the vertices are used when drawing. The default mode 'fan' is sufficient for simple convex polygons. |
| usage | SpriteBatchUsage | The expected usage of the Mesh. The specified usage mode affects the Mesh's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The new mesh. |

love.graphics.newMesh(vertexcount, texture, mode)

| name | type | description |
| --- | --- | --- |
| vertexcount | number | The total number of vertices the Mesh will use. Each vertex is initialized to {0,0, 0,0, 255,255,255,255}. |
| texture | Texture | The Image or Canvas to use when drawing the Mesh. May be nil to use no texture. |
| mode | MeshDrawMode | How the vertices are used when drawing. The default mode 'fan' is sufficient for simple convex polygons. |

| name | type | description |
| --- | --- | --- |
| mesh | Mesh | The new mesh. |


love.graphics.newParticleSystem

Creates a new ParticleSystem.

love.graphics.newParticleSystem(image, buffer)

| name | type | description |
| --- | --- | --- |
| image | Image | The image to use. |
| buffer | number | The max number of particles at the same time. |

| name | type | description |
| --- | --- | --- |
| system | ParticleSystem | A new ParticleSystem. |

love.graphics.newParticleSystem(texture, buffer)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The texture (Image or Canvas) to use. |
| buffer | number | The max number of particles at the same time. |

| name | type | description |
| --- | --- | --- |
| system | ParticleSystem | A new ParticleSystem. |


love.graphics.newQuad

Creates a new Quad.

The purpose of a Quad is to use a fraction of an image to draw objects, as opposed to drawing entire image. It is most useful for sprite sheets and atlases: in a sprite atlas, multiple sprites reside in same image, quad is used to draw a specific sprite from that image; in animated sprites with all frames residing in the same image, quad is used to draw specific frame from the animation.

love.graphics.newQuad(x, y, width, height, sw, sh)

| name | type | description |
| --- | --- | --- |
| x | number | The top-left position in the Image along the x-axis. |
| y | number | The top-left position in the Image along the y-axis. |
| width | number | The width of the Quad in the Image. (Must be greater than 0.) |
| height | number | The height of the Quad in the Image. (Must be greater than 0.) |
| sw | number | The reference width, the width of the Image. (Must be greater than 0.) |
| sh | number | The reference height, the height of the Image. (Must be greater than 0.) |

| name | type | description |
| --- | --- | --- |
| quad | Quad | The new Quad. |

love.graphics.newQuad(x, y, width, height, texture)

| name | type | description |
| --- | --- | --- |
| x | number | The top-left position in the Image along the x-axis. |
| y | number | The top-left position in the Image along the y-axis. |
| width | number | The width of the Quad in the Image. (Must be greater than 0.) |
| height | number | The height of the Quad in the Image. (Must be greater than 0.) |
| texture | Texture | The texture whose width and height will be used as the reference width and height. |

| name | type | description |
| --- | --- | --- |
| quad | Quad | The new Quad. |


love.graphics.newShader

Creates a new Shader object for hardware-accelerated vertex and pixel effects. A Shader contains either vertex shader code, pixel shader code, or both.

Shaders are small programs which are run on the graphics card when drawing. Vertex shaders are run once for each vertex (for example, an image has 4 vertices - one at each corner. A Mesh might have many more.) Pixel shaders are run once for each pixel on the screen which the drawn object touches. Pixel shader code is executed after all the object's vertices have been processed by the vertex shader.

love.graphics.newShader(code)

| name | type | description |
| --- | --- | --- |
| code | string | The pixel shader or vertex shader code, or a filename pointing to a file with the code. |

| name | type | description |
| --- | --- | --- |
| shader | Shader | A Shader object for use in drawing operations. |

love.graphics.newShader(pixelcode, vertexcode)

| name | type | description |
| --- | --- | --- |
| pixelcode | string | The pixel shader code, or a filename pointing to a file with the code. |
| vertexcode | string | The vertex shader code, or a filename pointing to a file with the code. |

| name | type | description |
| --- | --- | --- |
| shader | Shader | A Shader object for use in drawing operations. |


love.graphics.newSpriteBatch

Creates a new SpriteBatch object.

love.graphics.newSpriteBatch(image, maxsprites)

| name | type | description |
| --- | --- | --- |
| image | Image | The Image to use for the sprites. |
| maxsprites | number | The maximum number of sprites that the SpriteBatch can contain at any given time. Since version 11.0, additional sprites added past this number will automatically grow the spritebatch. |

| name | type | description |
| --- | --- | --- |
| spriteBatch | SpriteBatch | The new SpriteBatch. |

love.graphics.newSpriteBatch(image, maxsprites, usage)

| name | type | description |
| --- | --- | --- |
| image | Image | The Image to use for the sprites. |
| maxsprites | number | The maximum number of sprites that the SpriteBatch can contain at any given time. Since version 11.0, additional sprites added past this number will automatically grow the spritebatch. |
| usage | SpriteBatchUsage | The expected usage of the SpriteBatch. The specified usage mode affects the SpriteBatch's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| spriteBatch | SpriteBatch | The new SpriteBatch. |

love.graphics.newSpriteBatch(texture, maxsprites, usage)

| name | type | description |
| --- | --- | --- |
| texture | Texture | The Image or Canvas to use for the sprites. |
| maxsprites | number | The maximum number of sprites that the SpriteBatch can contain at any given time. Since version 11.0, additional sprites added past this number will automatically grow the spritebatch. |
| usage | SpriteBatchUsage | The expected usage of the SpriteBatch. The specified usage mode affects the SpriteBatch's memory usage and performance. |

| name | type | description |
| --- | --- | --- |
| spriteBatch | SpriteBatch | The new SpriteBatch. |


love.graphics.newText

Creates a new drawable Text object.

love.graphics.newText(font, textstring)

| name | type | description |
| --- | --- | --- |
| font | Font | The font to use for the text. |
| textstring | string | The initial string of text that the new Text object will contain. May be nil. |

| name | type | description |
| --- | --- | --- |
| text | Text | The new drawable Text object. |

love.graphics.newText(font, coloredtext)

| name | type | description |
| --- | --- | --- |
| font | Font | The font to use for the text. |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |

| name | type | description |
| --- | --- | --- |
| text | Text | The new drawable Text object. |


love.graphics.newVideo

Creates a new drawable Video. Currently only Ogg Theora video files are supported.

love.graphics.newVideo(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The file path to the Ogg Theora video file. |

| name | type | description |
| --- | --- | --- |
| video | Video | A new Video. |

love.graphics.newVideo(videostream)

| name | type | description |
| --- | --- | --- |
| videostream | VideoStream | A video stream object. |

| name | type | description |
| --- | --- | --- |
| video | Video | A new Video. |

love.graphics.newVideo(filename, settings)

| name | type | description |
| --- | --- | --- |
| filename | string | The file path to the Ogg Theora video file (or VideoStream). |
| settings | table | A table containing the following fields: |

| name | type | description |
| --- | --- | --- |
| video | Video | A new Video. |

love.graphics.newVideo(filename, loadaudio)

| name | type | description |
| --- | --- | --- |
| filename | string | The file path to the Ogg Theora video file. |
| loadaudio | boolean | Whether to try to load the video's audio into an audio Source. If not explicitly set to true or false, it will try without causing an error if the video has no audio. |

| name | type | description |
| --- | --- | --- |
| video | Video | A new Video. |

love.graphics.newVideo(videostream, loadaudio)

| name | type | description |
| --- | --- | --- |
| videostream | VideoStream | A video stream object. |
| loadaudio | boolean | Whether to try to load the video's audio into an audio Source. If not explicitly set to true or false, it will try without causing an error if the video has no audio. |

| name | type | description |
| --- | --- | --- |
| video | Video | A new Video. |


love.graphics.newVolumeImage

Creates a new volume (3D) Image.

Volume images are 3D textures with width, height, and depth. They can't be rendered directly, they can only be used in Shader code (and sent to the shader via Shader:send).

To use a volume image in a Shader, it must be declared as a VolumeImage or sampler3D type (instead of Image or sampler2D). The Texel(VolumeImage image, vec3 texcoords) shader function must be used to get pixel colors from the volume image. The vec3 argument is a normalized texture coordinate with the z component representing the depth to sample at (ranging from 1).

Volume images are typically used as lookup tables in shaders for color grading, for example, because sampling using a texture coordinate that is partway in between two pixels can interpolate across all 3 dimensions in the volume image, resulting in a smooth gradient even when a small-sized volume image is used as the lookup table.

Array images are a much better choice than volume images for storing multiple different sprites in a single array image for directly drawing them.

love.graphics.newVolumeImage(layers, settings)

| name | type | description |
| --- | --- | --- |
| layers | table | A table containing filepaths to images (or File, FileData, ImageData, or CompressedImageData objects), in an array. A table of tables can also be given, where each sub-table represents a single mipmap level and contains all layers for that mipmap. |
| settings | table | Optional table of settings to configure the volume image, containing the following fields: |

| name | type | description |
| --- | --- | --- |
| image | Image | A volume Image object. |


love.graphics.origin

Resets the current coordinate transformation.

This function is always used to reverse any previous calls to love.graphics.rotate, love.graphics.scale, love.graphics.shear or love.graphics.translate. It returns the current transformation state to its defaults.

love.graphics.origin()


love.graphics.points

Draws one or more points.

love.graphics.points(x, y, ...)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the first point on the x-axis. |
| y | number | The position of the first point on the y-axis. |
| ... | number | The x and y coordinates of additional points. |

love.graphics.points(points)

| name | type | description |
| --- | --- | --- |
| points | table | A table containing multiple point positions, in the form of {x, y, ...}. |

love.graphics.points(points)

| name | type | description |
| --- | --- | --- |
| points | table | A table containing multiple individually colored points, in the form of {point, ...}. |


love.graphics.polygon

Draw a polygon.

Following the mode argument, this function can accept multiple numeric arguments or a single table of numeric arguments. In either case the arguments are interpreted as alternating x and y coordinates of the polygon's vertices.

love.graphics.polygon(mode, ...)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the polygon. |
| ... | number | The vertices of the polygon. |

love.graphics.polygon(mode, vertices)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the polygon. |
| vertices | table | The vertices of the polygon as a table. |


love.graphics.pop

Pops the current coordinate transformation from the transformation stack.

This function is always used to reverse a previous push operation. It returns the current transformation state to what it was before the last preceding push.

love.graphics.pop()


love.graphics.present

Displays the results of drawing operations on the screen.

This function is used when writing your own love.run function. It presents all the results of your drawing operations on the screen. See the example in love.run for a typical use of this function.

love.graphics.present()


love.graphics.print

Draws text on screen. If no Font is set, one will be created and set (once) if needed.

As of LOVE 0.7.1, when using translation and scaling functions while drawing text, this function assumes the scale occurs first.  If you don't script with this in mind, the text won't be in the right position, or possibly even on screen.

love.graphics.print and love.graphics.printf both support UTF-8 encoding. You'll also need a proper Font for special characters.

In versions prior to 11.0, color and byte component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.print(text, x, y, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| text | string | The text to draw. |
| x | number | The position to draw the object (x-axis). |
| y | number | The position to draw the object (y-axis). |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.print(coloredtext, x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| x | number | The position of the text on the x-axis. |
| y | number | The position of the text on the y-axis. |
| angle | number | The orientation of the text in radians. |
| sx | number | Scale factor on the x-axis. |
| sy | number | Scale factor on the y-axis. |
| ox | number | Origin offset on the x-axis. |
| oy | number | Origin offset on the y-axis. |
| kx | number | Shearing / skew factor on the x-axis. |
| ky | number | Shearing / skew factor on the y-axis. |

love.graphics.print(text, transform)

| name | type | description |
| --- | --- | --- |
| text | string | The text to draw. |
| transform | Transform | Transformation object. |

love.graphics.print(coloredtext, transform)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| transform | Transform | Transformation object. |

love.graphics.print(text, font, transform)

| name | type | description |
| --- | --- | --- |
| text | string | The text to draw. |
| font | Font | The Font object to use. |
| transform | Transform | Transformation object. |

love.graphics.print(coloredtext, font, transform)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| font | Font | The Font object to use. |
| transform | Transform | Transformation object. |


love.graphics.printf

Draws formatted text, with word wrap and alignment.

See additional notes in love.graphics.print.

The word wrap limit is applied before any scaling, rotation, and other coordinate transformations. Therefore the amount of text per line stays constant given the same wrap limit, even if the scale arguments change.

In version 0.9.2 and earlier, wrapping was implemented by breaking up words by spaces and putting them back together to make sure things fit nicely within the limit provided. However, due to the way this is done, extra spaces between words would end up missing when printed on the screen, and some lines could overflow past the provided wrap limit. In version 0.10.0 and newer this is no longer the case.

In versions prior to 11.0, color and byte component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.printf(text, x, y, limit, align, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| text | string | A text string. |
| x | number | The position on the x-axis. |
| y | number | The position on the y-axis. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.printf(text, font, x, y, limit, align, r, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| text | string | A text string. |
| font | Font | The Font object to use. |
| x | number | The position on the x-axis. |
| y | number | The position on the y-axis. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |
| r | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.printf(text, transform, limit, align)

| name | type | description |
| --- | --- | --- |
| text | string | A text string. |
| transform | Transform | Transformation object. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |

love.graphics.printf(text, font, transform, limit, align)

| name | type | description |
| --- | --- | --- |
| text | string | A text string. |
| font | Font | The Font object to use. |
| transform | Transform | Transformation object. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |

love.graphics.printf(coloredtext, x, y, limit, align, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| x | number | The position of the text (x-axis). |
| y | number | The position of the text (y-axis). |
| limit | number | The maximum width in pixels of the text before it gets automatically wrapped to a new line. |
| align | AlignMode | The alignment of the text. |
| angle | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing / skew factor (x-axis). |
| ky | number | Shearing / skew factor (y-axis). |

love.graphics.printf(coloredtext, font, x, y, limit, align, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| font | Font | The Font object to use. |
| x | number | The position on the x-axis. |
| y | number | The position on the y-axis. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |
| angle | number | Orientation (radians). |
| sx | number | Scale factor (x-axis). |
| sy | number | Scale factor (y-axis). |
| ox | number | Origin offset (x-axis). |
| oy | number | Origin offset (y-axis). |
| kx | number | Shearing factor (x-axis). |
| ky | number | Shearing factor (y-axis). |

love.graphics.printf(coloredtext, transform, limit, align)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| transform | Transform | Transformation object. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |

love.graphics.printf(coloredtext, font, transform, limit, align)

| name | type | description |
| --- | --- | --- |
| coloredtext | table | A table containing colors and strings to add to the object, in the form of {color1, string1, color2, string2, ...}. |
| font | Font | The Font object to use. |
| transform | Transform | Transformation object. |
| limit | number | Wrap the line after this many horizontal pixels. |
| align | AlignMode | The alignment. |


love.graphics.push

Copies and pushes the current coordinate transformation to the transformation stack.

This function is always used to prepare for a corresponding pop operation later. It stores the current coordinate transformation state into the transformation stack and keeps it active. Later changes to the transformation can be undone by using the pop operation, which returns the coordinate transform to the state it was in before calling push.

love.graphics.push()

love.graphics.push(stack)

| name | type | description |
| --- | --- | --- |
| stack | StackType | The type of stack to push (e.g. just transformation state, or all love.graphics state). |


love.graphics.rectangle

Draws a rectangle.

love.graphics.rectangle(mode, x, y, width, height)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the rectangle. |
| x | number | The position of top-left corner along the x-axis. |
| y | number | The position of top-left corner along the y-axis. |
| width | number | Width of the rectangle. |
| height | number | Height of the rectangle. |

love.graphics.rectangle(mode, x, y, width, height, rx, ry, segments)

| name | type | description |
| --- | --- | --- |
| mode | DrawMode | How to draw the rectangle. |
| x | number | The position of top-left corner along the x-axis. |
| y | number | The position of top-left corner along the y-axis. |
| width | number | Width of the rectangle. |
| height | number | Height of the rectangle. |
| rx | number | The x-axis radius of each round corner. Cannot be greater than half the rectangle's width. |
| ry | number | The y-axis radius of each round corner. Cannot be greater than half the rectangle's height. |
| segments | number | The number of segments used for drawing the round corners. A default amount will be chosen if no number is given. |


love.graphics.replaceTransform

Replaces the current coordinate transformation with the given Transform object.

love.graphics.replaceTransform(transform)

| name | type | description |
| --- | --- | --- |
| transform | Transform | The Transform object to replace the current graphics coordinate transform with. |


love.graphics.reset

Resets the current graphics settings.

Calling reset makes the current drawing color white, the current background color black, disables any active color component masks, disables wireframe mode and resets the current graphics transformation to the origin. It also sets both the point and line drawing modes to smooth and their sizes to 1.0.

love.graphics.reset()


love.graphics.rotate

Rotates the coordinate system in two dimensions.

Calling this function affects all future drawing operations by rotating the coordinate system around the origin by the given amount of radians. This change lasts until love.draw() exits.

love.graphics.rotate(angle)

| name | type | description |
| --- | --- | --- |
| angle | number | The amount to rotate the coordinate system in radians. |


love.graphics.scale

Scales the coordinate system in two dimensions.

By default the coordinate system in LÖVE corresponds to the display pixels in horizontal and vertical directions one-to-one, and the x-axis increases towards the right while the y-axis increases downwards. Scaling the coordinate system changes this relation.

After scaling by sx and sy, all coordinates are treated as if they were multiplied by sx and sy. Every result of a drawing operation is also correspondingly scaled, so scaling by (2, 2) for example would mean making everything twice as large in both x- and y-directions. Scaling by a negative value flips the coordinate system in the corresponding direction, which also means everything will be drawn flipped or upside down, or both. Scaling by zero is not a useful operation.

Scale and translate are not commutative operations, therefore, calling them in different orders will change the outcome.

Scaling lasts until love.draw() exits.

love.graphics.scale(sx, sy)

| name | type | description |
| --- | --- | --- |
| sx | number | The scaling in the direction of the x-axis. |
| sy | number | The scaling in the direction of the y-axis. If omitted, it defaults to same as parameter sx. |


love.graphics.setBackgroundColor

Sets the background color.

love.graphics.setBackgroundColor(red, green, blue, alpha)

| name | type | description |
| --- | --- | --- |
| red | number | The red component (0-1). |
| green | number | The green component (0-1). |
| blue | number | The blue component (0-1). |
| alpha | number | The alpha component (0-1). |

love.graphics.setBackgroundColor(rgba)

| name | type | description |
| --- | --- | --- |
| rgba | table | A numerical indexed table with the red, green, blue and alpha values as numbers. The alpha is optional and defaults to 1 if it is left out. |


love.graphics.setBlendMode

Sets the blending mode.

love.graphics.setBlendMode(mode)

| name | type | description |
| --- | --- | --- |
| mode | BlendMode | The blend mode to use. |

love.graphics.setBlendMode(mode, alphamode)

| name | type | description |
| --- | --- | --- |
| mode | BlendMode | The blend mode to use. |
| alphamode | BlendAlphaMode | What to do with the alpha of drawn objects when blending. |


love.graphics.setCanvas

Captures drawing operations to a Canvas.

love.graphics.setCanvas(canvas, mipmap)

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | The new target. |
| mipmap | number | The mipmap level to render to, for Canvases with mipmaps. |

love.graphics.setCanvas()

love.graphics.setCanvas(canvas1, canvas2, ...)

| name | type | description |
| --- | --- | --- |
| canvas1 | Canvas | The first render target. |
| canvas2 | Canvas | The second render target. |
| ... | Canvas | More canvases. |

love.graphics.setCanvas(canvas, slice, mipmap)

| name | type | description |
| --- | --- | --- |
| canvas | Canvas | The new render target. |
| slice | number | For cubemaps this is the cube face index to render to (between 1 and 6). For Array textures this is the array layer. For volume textures this is the depth slice. 2D canvases should use a value of 1. |
| mipmap | number | The mipmap level to render to, for Canvases with mipmaps. |

love.graphics.setCanvas(setup)

| name | type | description |
| --- | --- | --- |
| setup | table | A table specifying the active Canvas(es), their mipmap levels and active layers if applicable, and whether to use a stencil and/or depth buffer. |


love.graphics.setColor

Sets the color used for drawing.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

love.graphics.setColor(red, green, blue, alpha)

| name | type | description |
| --- | --- | --- |
| red | number | The amount of red. |
| green | number | The amount of green. |
| blue | number | The amount of blue. |
| alpha | number | The amount of alpha.  The alpha value will be applied to all subsequent draw operations, even the drawing of an image. |

love.graphics.setColor(rgba)

| name | type | description |
| --- | --- | --- |
| rgba | table | A numerical indexed table with the red, green, blue and alpha values as numbers. The alpha is optional and defaults to 1 if it is left out. |


love.graphics.setColorMask

Sets the color mask. Enables or disables specific color components when rendering and clearing the screen. For example, if '''red''' is set to '''false''', no further changes will be made to the red component of any pixels.

love.graphics.setColorMask(red, green, blue, alpha)

| name | type | description |
| --- | --- | --- |
| red | boolean | Render red component. |
| green | boolean | Render green component. |
| blue | boolean | Render blue component. |
| alpha | boolean | Render alpha component. |

love.graphics.setColorMask()


love.graphics.setDefaultFilter

Sets the default scaling filters used with Images, Canvases, and Fonts.

love.graphics.setDefaultFilter(min, mag, anisotropy)

| name | type | description |
| --- | --- | --- |
| min | FilterMode | Filter mode used when scaling the image down. |
| mag | FilterMode | Filter mode used when scaling the image up. |
| anisotropy | number | Maximum amount of Anisotropic Filtering used. |


love.graphics.setDepthMode

Configures depth testing and writing to the depth buffer.

This is low-level functionality designed for use with custom vertex shaders and Meshes with custom vertex attributes. No higher level APIs are provided to set the depth of 2D graphics such as shapes, lines, and Images.

love.graphics.setDepthMode(comparemode, write)

| name | type | description |
| --- | --- | --- |
| comparemode | CompareMode | Depth comparison mode used for depth testing. |
| write | boolean | Whether to write update / write values to the depth buffer when rendering. |

love.graphics.setDepthMode()


love.graphics.setFont

Set an already-loaded Font as the current font or create and load a new one from the file and size.

It's recommended that Font objects are created with love.graphics.newFont in the loading stage and then passed to this function in the drawing stage.

love.graphics.setFont(font)

| name | type | description |
| --- | --- | --- |
| font | Font | The Font object to use. |


love.graphics.setFrontFaceWinding

Sets whether triangles with clockwise- or counterclockwise-ordered vertices are considered front-facing.

This is designed for use in combination with Mesh face culling. Other love.graphics shapes, lines, and sprites are not guaranteed to have a specific winding order to their internal vertices.

love.graphics.setFrontFaceWinding(winding)

| name | type | description |
| --- | --- | --- |
| winding | VertexWinding | The winding mode to use. The default winding is counterclockwise ('ccw'). |


love.graphics.setLineJoin

Sets the line join style. See LineJoin for the possible options.

love.graphics.setLineJoin(join)

| name | type | description |
| --- | --- | --- |
| join | LineJoin | The LineJoin to use. |


love.graphics.setLineStyle

Sets the line style.

love.graphics.setLineStyle(style)

| name | type | description |
| --- | --- | --- |
| style | LineStyle | The LineStyle to use. Line styles include smooth and rough. |


love.graphics.setLineWidth

Sets the line width.

love.graphics.setLineWidth(width)

| name | type | description |
| --- | --- | --- |
| width | number | The width of the line. |


love.graphics.setMeshCullMode

Sets whether back-facing triangles in a Mesh are culled.

This is designed for use with low level custom hardware-accelerated 3D rendering via custom vertex attributes on Meshes, custom vertex shaders, and depth testing with a depth buffer.

By default, both front- and back-facing triangles in Meshes are rendered.

love.graphics.setMeshCullMode(mode)

| name | type | description |
| --- | --- | --- |
| mode | CullMode | The Mesh face culling mode to use (whether to render everything, cull back-facing triangles, or cull front-facing triangles). |


love.graphics.setNewFont

Creates and sets a new Font.

love.graphics.setNewFont(size)

| name | type | description |
| --- | --- | --- |
| size | number | The size of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | The new font. |

love.graphics.setNewFont(filename, size)

| name | type | description |
| --- | --- | --- |
| filename | string | The path and name of the file with the font. |
| size | number | The size of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | The new font. |

love.graphics.setNewFont(file, size)

| name | type | description |
| --- | --- | --- |
| file | File | A File with the font. |
| size | number | The size of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | The new font. |

love.graphics.setNewFont(data, size)

| name | type | description |
| --- | --- | --- |
| data | Data | A Data with the font. |
| size | number | The size of the font. |

| name | type | description |
| --- | --- | --- |
| font | Font | The new font. |

love.graphics.setNewFont(rasterizer)

| name | type | description |
| --- | --- | --- |
| rasterizer | Rasterizer | A rasterizer. |

| name | type | description |
| --- | --- | --- |
| font | Font | The new font. |


love.graphics.setPointSize

Sets the point size.

love.graphics.setPointSize(size)

| name | type | description |
| --- | --- | --- |
| size | number | The new point size. |


love.graphics.setScissor

Sets or disables scissor.

The scissor limits the drawing area to a specified rectangle. This affects all graphics calls, including love.graphics.clear.

The dimensions of the scissor is unaffected by graphical transformations (translate, scale, ...).

love.graphics.setScissor(x, y, width, height)

| name | type | description |
| --- | --- | --- |
| x | number | x coordinate of upper left corner. |
| y | number | y coordinate of upper left corner. |
| width | number | width of clipping rectangle. |
| height | number | height of clipping rectangle. |

love.graphics.setScissor()


love.graphics.setShader

Sets or resets a Shader as the current pixel effect or vertex shaders. All drawing operations until the next ''love.graphics.setShader'' will be drawn using the Shader object specified.

love.graphics.setShader(shader)

| name | type | description |
| --- | --- | --- |
| shader | Shader | The new shader. |

love.graphics.setShader()


love.graphics.setStencilTest

Configures or disables stencil testing.

When stencil testing is enabled, the geometry of everything that is drawn afterward will be clipped / stencilled out based on a comparison between the arguments of this function and the stencil value of each pixel that the geometry touches. The stencil values of pixels are affected via love.graphics.stencil.

love.graphics.setStencilTest(comparemode, comparevalue)

| name | type | description |
| --- | --- | --- |
| comparemode | CompareMode | The type of comparison to make for each pixel. |
| comparevalue | number | The value to use when comparing with the stencil value of each pixel. Must be between 0 and 255. |

love.graphics.setStencilTest()


love.graphics.setWireframe

Sets whether wireframe lines will be used when drawing.

love.graphics.setWireframe(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable wireframe mode when drawing, false to disable it. |


love.graphics.shear

Shears the coordinate system.

love.graphics.shear(kx, ky)

| name | type | description |
| --- | --- | --- |
| kx | number | The shear factor on the x-axis. |
| ky | number | The shear factor on the y-axis. |


love.graphics.stencil

Draws geometry as a stencil.

The geometry drawn by the supplied function sets invisible stencil values of pixels, instead of setting pixel colors. The stencil buffer (which contains those stencil values) can act like a mask / stencil - love.graphics.setStencilTest can be used afterward to determine how further rendering is affected by the stencil values in each pixel.

Stencil values are integers within the range of 255.

love.graphics.stencil(stencilfunction, action, value, keepvalues)

| name | type | description |
| --- | --- | --- |
| stencilfunction | function | Function which draws geometry. The stencil values of pixels, rather than the color of each pixel, will be affected by the geometry. |
| action | StencilAction | How to modify any stencil values of pixels that are touched by what's drawn in the stencil function. |
| value | number | The new stencil value to use for pixels if the 'replace' stencil action is used. Has no effect with other stencil actions. Must be between 0 and 255. |
| keepvalues | boolean | True to preserve old stencil values of pixels, false to re-set every pixel's stencil value to 0 before executing the stencil function. love.graphics.clear will also re-set all stencil values. |


love.graphics.transformPoint

Converts the given 2D position from global coordinates into screen-space.

This effectively applies the current graphics transformations to the given position. A similar Transform:transformPoint method exists for Transform objects.

love.graphics.transformPoint(globalX, globalY)

| name | type | description |
| --- | --- | --- |
| globalX | number | The x component of the position in global coordinates. |
| globalY | number | The y component of the position in global coordinates. |

| name | type | description |
| --- | --- | --- |
| screenX | number | The x component of the position with graphics transformations applied. |
| screenY | number | The y component of the position with graphics transformations applied. |


love.graphics.translate

Translates the coordinate system in two dimensions.

When this function is called with two numbers, dx, and dy, all the following drawing operations take effect as if their x and y coordinates were x+dx and y+dy.

Scale and translate are not commutative operations, therefore, calling them in different orders will change the outcome.

This change lasts until love.draw() exits or else a love.graphics.pop reverts to a previous love.graphics.push.

Translating using whole numbers will prevent tearing/blurring of images and fonts draw after translating.

love.graphics.translate(dx, dy)

| name | type | description |
| --- | --- | --- |
| dx | number | The translation relative to the x-axis. |
| dy | number | The translation relative to the y-axis. |


love.graphics.validateShader

Validates shader code. Check if specified shader code does not contain any errors.

love.graphics.validateShader(gles, code)

| name | type | description |
| --- | --- | --- |
| gles | boolean | Validate code as GLSL ES shader. |
| code | string | The pixel shader or vertex shader code, or a filename pointing to a file with the code. |

| name | type | description |
| --- | --- | --- |
| status | boolean | true if specified shader code doesn't contain any errors. false otherwise. |
| message | string | Reason why shader code validation failed (or nil if validation succeded). |

love.graphics.validateShader(gles, pixelcode, vertexcode)

| name | type | description |
| --- | --- | --- |
| gles | boolean | Validate code as GLSL ES shader. |
| pixelcode | string | The pixel shader code, or a filename pointing to a file with the code. |
| vertexcode | string | The vertex shader code, or a filename pointing to a file with the code. |

| name | type | description |
| --- | --- | --- |
| status | boolean | true if specified shader code doesn't contain any errors. false otherwise. |
| message | string | Reason why shader code validation failed (or nil if validation succeded). |


love.hasDeprecationOutput

Gets whether LÖVE displays warnings when using deprecated functionality. It is disabled by default in fused mode, and enabled by default otherwise.

When deprecation output is enabled, the first use of a formally deprecated LÖVE API will show a message at the bottom of the screen for a short time, and print the message to the console.

love.hasDeprecationOutput()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | Whether deprecation output is enabled. |


love.image.isCompressed

Determines whether a file can be loaded as CompressedImageData.

love.image.isCompressed(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the potentially compressed image file. |

| name | type | description |
| --- | --- | --- |
| compressed | boolean | Whether the file can be loaded as CompressedImageData or not. |

love.image.isCompressed(fileData)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | A FileData potentially containing a compressed image. |

| name | type | description |
| --- | --- | --- |
| compressed | boolean | Whether the FileData can be loaded as CompressedImageData or not. |


love.image.newCompressedData

Create a new CompressedImageData object from a compressed image file. LÖVE supports several compressed texture formats, enumerated in the CompressedImageFormat page.

love.image.newCompressedData(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the compressed image file. |

| name | type | description |
| --- | --- | --- |
| compressedImageData | CompressedImageData | The new CompressedImageData object. |

love.image.newCompressedData(fileData)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | A FileData containing a compressed image. |

| name | type | description |
| --- | --- | --- |
| compressedImageData | CompressedImageData | The new CompressedImageData object. |


love.image.newImageData

Creates a new ImageData object.

love.image.newImageData(width, height)

| name | type | description |
| --- | --- | --- |
| width | number | The width of the ImageData. |
| height | number | The height of the ImageData. |

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The new blank ImageData object. Each pixel's color values, (including the alpha values!) will be set to zero. |

love.image.newImageData(width, height, format, data)

| name | type | description |
| --- | --- | --- |
| width | number | The width of the ImageData. |
| height | number | The height of the ImageData. |
| format | PixelFormat | The pixel format of the ImageData. |
| data | string | Optional raw byte data to load into the ImageData, in the format specified by ''format''. |

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The new ImageData object. |

love.image.newImageData(width, height, data)

| name | type | description |
| --- | --- | --- |
| width | number | The width of the ImageData. |
| height | number | The height of the ImageData. |
| data | string | The data to load into the ImageData (RGBA bytes, left to right and top to bottom). |

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The new ImageData object. |

love.image.newImageData(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the image file. |

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The new ImageData object. |

love.image.newImageData(filedata)

| name | type | description |
| --- | --- | --- |
| filedata | FileData | The encoded file data to decode into image data. |

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The new ImageData object. |


love.isVersionCompatible

Gets whether the given version is compatible with the current running version of LÖVE.

love.isVersionCompatible(version)

| name | type | description |
| --- | --- | --- |
| version | string | The version to check (for example '11.3' or '0.10.2'). |

| name | type | description |
| --- | --- | --- |
| compatible | boolean | Whether the given version is compatible with the current running version of LÖVE. |

love.isVersionCompatible(major, minor, revision)

| name | type | description |
| --- | --- | --- |
| major | number | The major version to check (for example 11 for 11.3 or 0 for 0.10.2). |
| minor | number | The minor version to check (for example 3 for 11.3 or 10 for 0.10.2). |
| revision | number | The revision of version to check (for example 0 for 11.3 or 2 for 0.10.2). |

| name | type | description |
| --- | --- | --- |
| compatible | boolean | Whether the given version is compatible with the current running version of LÖVE. |


love.joystick.getGamepadMappingString

Gets the full gamepad mapping string of the Joysticks which have the given GUID, or nil if the GUID isn't recognized as a gamepad.

The mapping string contains binding information used to map the Joystick's buttons an axes to the standard gamepad layout, and can be used later with love.joystick.loadGamepadMappings.

love.joystick.getGamepadMappingString(guid)

| name | type | description |
| --- | --- | --- |
| guid | string | The GUID value to get the mapping string for. |

| name | type | description |
| --- | --- | --- |
| mappingstring | string | A string containing the Joystick's gamepad mappings, or nil if the GUID is not recognized as a gamepad. |


love.joystick.getJoystickCount

Gets the number of connected joysticks.

love.joystick.getJoystickCount()

| name | type | description |
| --- | --- | --- |
| joystickcount | number | The number of connected joysticks. |


love.joystick.getJoysticks

Gets a list of connected Joysticks.

love.joystick.getJoysticks()

| name | type | description |
| --- | --- | --- |
| joysticks | table | The list of currently connected Joysticks. |


love.joystick.loadGamepadMappings

Loads a gamepad mappings string or file created with love.joystick.saveGamepadMappings.

It also recognizes any SDL gamecontroller mapping string, such as those created with Steam's Big Picture controller configure interface, or this nice database. If a new mapping is loaded for an already known controller GUID, the later version will overwrite the one currently loaded.

love.joystick.loadGamepadMappings(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename to load the mappings string from. |

love.joystick.loadGamepadMappings(mappings)

| name | type | description |
| --- | --- | --- |
| mappings | string | The mappings string to load. |


love.joystick.saveGamepadMappings

Saves the virtual gamepad mappings of all recognized as gamepads and have either been recently used or their gamepad bindings have been modified.

The mappings are stored as a string for use with love.joystick.loadGamepadMappings.

love.joystick.saveGamepadMappings(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename to save the mappings string to. |

| name | type | description |
| --- | --- | --- |
| mappings | string | The mappings string that was written to the file. |

love.joystick.saveGamepadMappings()

| name | type | description |
| --- | --- | --- |
| mappings | string | The mappings string. |


love.joystick.setGamepadMapping

Binds a virtual gamepad input to a button, axis or hat for all Joysticks of a certain type. For example, if this function is used with a GUID returned by a Dualshock 3 controller in OS X, the binding will affect Joystick:getGamepadAxis and Joystick:isGamepadDown for ''all'' Dualshock 3 controllers used with the game when run in OS X.

LÖVE includes built-in gamepad bindings for many common controllers. This function lets you change the bindings or add new ones for types of Joysticks which aren't recognized as gamepads by default.

The virtual gamepad buttons and axes are designed around the Xbox 360 controller layout.

love.joystick.setGamepadMapping(guid, button, inputtype, inputindex, hatdir)

| name | type | description |
| --- | --- | --- |
| guid | string | The OS-dependent GUID for the type of Joystick the binding will affect. |
| button | GamepadButton | The virtual gamepad button to bind. |
| inputtype | JoystickInputType | The type of input to bind the virtual gamepad button to. |
| inputindex | number | The index of the axis, button, or hat to bind the virtual gamepad button to. |
| hatdir | JoystickHat | The direction of the hat, if the virtual gamepad button will be bound to a hat. nil otherwise. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the virtual gamepad button was successfully bound. |

love.joystick.setGamepadMapping(guid, axis, inputtype, inputindex, hatdir)

| name | type | description |
| --- | --- | --- |
| guid | string | The OS-dependent GUID for the type of Joystick the binding will affect. |
| axis | GamepadAxis | The virtual gamepad axis to bind. |
| inputtype | JoystickInputType | The type of input to bind the virtual gamepad axis to. |
| inputindex | number | The index of the axis, button, or hat to bind the virtual gamepad axis to. |
| hatdir | JoystickHat | The direction of the hat, if the virtual gamepad axis will be bound to a hat. nil otherwise. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the virtual gamepad axis was successfully bound. |


love.joystickadded

Called when a Joystick is connected.

love.joystickadded(joystick)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The newly connected Joystick object. |


love.joystickaxis

Called when a joystick axis moves.

love.joystickaxis(joystick, axis, value)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| axis | number | The axis number. |
| value | number | The new axis value. |


love.joystickhat

Called when a joystick hat direction changes.

love.joystickhat(joystick, hat, direction)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| hat | number | The hat number. |
| direction | JoystickHat | The new hat direction. |


love.joystickpressed

Called when a joystick button is pressed.

love.joystickpressed(joystick, button)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| button | number | The button number. |


love.joystickreleased

Called when a joystick button is released.

love.joystickreleased(joystick, button)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The joystick object. |
| button | number | The button number. |


love.joystickremoved

Called when a Joystick is disconnected.

love.joystickremoved(joystick)

| name | type | description |
| --- | --- | --- |
| joystick | Joystick | The now-disconnected Joystick object. |


love.keyboard.getKeyFromScancode

Gets the key corresponding to the given hardware scancode.

Unlike key constants, Scancodes are keyboard layout-independent. For example the scancode 'w' will be generated if the key in the same place as the 'w' key on an American keyboard is pressed, no matter what the key is labelled or what the user's operating system settings are.

Scancodes are useful for creating default controls that have the same physical locations on on all systems.

love.keyboard.getKeyFromScancode(scancode)

| name | type | description |
| --- | --- | --- |
| scancode | Scancode | The scancode to get the key from. |

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | The key corresponding to the given scancode, or 'unknown' if the scancode doesn't map to a KeyConstant on the current system. |


love.keyboard.getScancodeFromKey

Gets the hardware scancode corresponding to the given key.

Unlike key constants, Scancodes are keyboard layout-independent. For example the scancode 'w' will be generated if the key in the same place as the 'w' key on an American keyboard is pressed, no matter what the key is labelled or what the user's operating system settings are.

Scancodes are useful for creating default controls that have the same physical locations on on all systems.

love.keyboard.getScancodeFromKey(key)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | The key to get the scancode from. |

| name | type | description |
| --- | --- | --- |
| scancode | Scancode | The scancode corresponding to the given key, or 'unknown' if the given key has no known physical representation on the current system. |


love.keyboard.hasKeyRepeat

Gets whether key repeat is enabled.

love.keyboard.hasKeyRepeat()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | Whether key repeat is enabled. |


love.keyboard.hasScreenKeyboard

Gets whether screen keyboard is supported.

love.keyboard.hasScreenKeyboard()

| name | type | description |
| --- | --- | --- |
| supported | boolean | Whether screen keyboard is supported. |


love.keyboard.hasTextInput

Gets whether text input events are enabled.

love.keyboard.hasTextInput()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | Whether text input events are enabled. |


love.keyboard.isDown

Checks whether a certain key is down. Not to be confused with love.keypressed or love.keyreleased.

love.keyboard.isDown(key)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | The key to check. |

| name | type | description |
| --- | --- | --- |
| down | boolean | True if the key is down, false if not. |

love.keyboard.isDown(key, ...)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | A key to check. |
| ... | KeyConstant | Additional keys to check. |

| name | type | description |
| --- | --- | --- |
| anyDown | boolean | True if any supplied key is down, false if not. |


love.keyboard.isScancodeDown

Checks whether the specified Scancodes are pressed. Not to be confused with love.keypressed or love.keyreleased.

Unlike regular KeyConstants, Scancodes are keyboard layout-independent. The scancode 'w' is used if the key in the same place as the 'w' key on an American keyboard is pressed, no matter what the key is labelled or what the user's operating system settings are.

love.keyboard.isScancodeDown(scancode, ...)

| name | type | description |
| --- | --- | --- |
| scancode | Scancode | A Scancode to check. |
| ... | Scancode | Additional Scancodes to check. |

| name | type | description |
| --- | --- | --- |
| down | boolean | True if any supplied Scancode is down, false if not. |


love.keyboard.setKeyRepeat

Enables or disables key repeat for love.keypressed. It is disabled by default.

love.keyboard.setKeyRepeat(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether repeat keypress events should be enabled when a key is held down. |


love.keyboard.setTextInput

Enables or disables text input events. It is enabled by default on Windows, Mac, and Linux, and disabled by default on iOS and Android.

On touch devices, this shows the system's native on-screen keyboard when it's enabled.

love.keyboard.setTextInput(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether text input events should be enabled. |

love.keyboard.setTextInput(enable, x, y, w, h)

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether text input events should be enabled. |
| x | number | Text rectangle x position. |
| y | number | Text rectangle y position. |
| w | number | Text rectangle width. |
| h | number | Text rectangle height. |


love.keypressed

Callback function triggered when a key is pressed.

love.keypressed(key, scancode, isrepeat)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | Character of the pressed key. |
| scancode | Scancode | The scancode representing the pressed key. |
| isrepeat | boolean | Whether this keypress event is a repeat. The delay between key repeats depends on the user's system settings. |

love.keypressed(key, isrepeat)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | Character of the key pressed. |
| isrepeat | boolean | Whether this keypress event is a repeat. The delay between key repeats depends on the user's system settings. |


love.keyreleased

Callback function triggered when a keyboard key is released.

love.keyreleased(key, scancode)

| name | type | description |
| --- | --- | --- |
| key | KeyConstant | Character of the released key. |
| scancode | Scancode | The scancode representing the released key. |


love.load

This function is called exactly once at the beginning of the game.

love.load(arg, unfilteredArg)

| name | type | description |
| --- | --- | --- |
| arg | table | Command-line arguments given to the game. |
| unfilteredArg | table | Unfiltered command-line arguments given to the executable (see #Notes). |


love.lowmemory

Callback function triggered when the system is running out of memory on mobile devices.

Mobile operating systems may forcefully kill the game if it uses too much memory, so any non-critical resource should be removed if possible (by setting all variables referencing the resources to '''nil'''), when this event is triggered. Sounds and images in particular tend to use the most memory.

love.lowmemory()


love.math.colorFromBytes

Converts a color from 0..255 to 0..1 range.

love.math.colorFromBytes(rb, gb, bb, ab)

| name | type | description |
| --- | --- | --- |
| rb | number | Red color component in 0..255 range. |
| gb | number | Green color component in 0..255 range. |
| bb | number | Blue color component in 0..255 range. |
| ab | number | Alpha color component in 0..255 range. |

| name | type | description |
| --- | --- | --- |
| r | number | Red color component in 0..1 range. |
| g | number | Green color component in 0..1 range. |
| b | number | Blue color component in 0..1 range. |
| a | number | Alpha color component in 0..1 range or nil if alpha is not specified. |


love.math.colorToBytes

Converts a color from 0..1 to 0..255 range.

love.math.colorToBytes(r, g, b, a)

| name | type | description |
| --- | --- | --- |
| r | number | Red color component. |
| g | number | Green color component. |
| b | number | Blue color component. |
| a | number | Alpha color component. |

| name | type | description |
| --- | --- | --- |
| rb | number | Red color component in 0..255 range. |
| gb | number | Green color component in 0..255 range. |
| bb | number | Blue color component in 0..255 range. |
| ab | number | Alpha color component in 0..255 range or nil if alpha is not specified. |


love.math.gammaToLinear

Converts a color from gamma-space (sRGB) to linear-space (RGB). This is useful when doing gamma-correct rendering and you need to do math in linear RGB in the few cases where LÖVE doesn't handle conversions automatically.

Read more about gamma-correct rendering here, here, and here.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

love.math.gammaToLinear(r, g, b)

| name | type | description |
| --- | --- | --- |
| r | number | The red channel of the sRGB color to convert. |
| g | number | The green channel of the sRGB color to convert. |
| b | number | The blue channel of the sRGB color to convert. |

| name | type | description |
| --- | --- | --- |
| lr | number | The red channel of the converted color in linear RGB space. |
| lg | number | The green channel of the converted color in linear RGB space. |
| lb | number | The blue channel of the converted color in linear RGB space. |

love.math.gammaToLinear(color)

| name | type | description |
| --- | --- | --- |
| color | table | An array with the red, green, and blue channels of the sRGB color to convert. |

| name | type | description |
| --- | --- | --- |
| lr | number | The red channel of the converted color in linear RGB space. |
| lg | number | The green channel of the converted color in linear RGB space. |
| lb | number | The blue channel of the converted color in linear RGB space. |

love.math.gammaToLinear(c)

| name | type | description |
| --- | --- | --- |
| c | number | The value of a color channel in sRGB space to convert. |

| name | type | description |
| --- | --- | --- |
| lc | number | The value of the color channel in linear RGB space. |


love.math.getRandomSeed

Gets the seed of the random number generator.

The seed is split into two numbers due to Lua's use of doubles for all number values - doubles can't accurately represent integer  values above 2^53, but the seed can be an integer value up to 2^64.

love.math.getRandomSeed()

| name | type | description |
| --- | --- | --- |
| low | number | Integer number representing the lower 32 bits of the random number generator's 64 bit seed value. |
| high | number | Integer number representing the higher 32 bits of the random number generator's 64 bit seed value. |


love.math.getRandomState

Gets the current state of the random number generator. This returns an opaque implementation-dependent string which is only useful for later use with love.math.setRandomState or RandomGenerator:setState.

This is different from love.math.getRandomSeed in that getRandomState gets the random number generator's current state, whereas getRandomSeed gets the previously set seed number.

love.math.getRandomState()

| name | type | description |
| --- | --- | --- |
| state | string | The current state of the random number generator, represented as a string. |


love.math.isConvex

Checks whether a polygon is convex.

PolygonShapes in love.physics, some forms of Meshes, and polygons drawn with love.graphics.polygon must be simple convex polygons.

love.math.isConvex(vertices)

| name | type | description |
| --- | --- | --- |
| vertices | table | The vertices of the polygon as a table in the form of {x1, y1, x2, y2, x3, y3, ...}. |

| name | type | description |
| --- | --- | --- |
| convex | boolean | Whether the given polygon is convex. |

love.math.isConvex(x1, y1, x2, y2, ...)

| name | type | description |
| --- | --- | --- |
| x1 | number | The position of the first vertex of the polygon on the x-axis. |
| y1 | number | The position of the first vertex of the polygon on the y-axis. |
| x2 | number | The position of the second vertex of the polygon on the x-axis. |
| y2 | number | The position of the second vertex of the polygon on the y-axis. |
| ... | number | Additional position of the vertex of the polygon on the x-axis and y-axis. |

| name | type | description |
| --- | --- | --- |
| convex | boolean | Whether the given polygon is convex. |


love.math.linearToGamma

Converts a color from linear-space (RGB) to gamma-space (sRGB). This is useful when storing linear RGB color values in an image, because the linear RGB color space has less precision than sRGB for dark colors, which can result in noticeable color banding when drawing.

In general, colors chosen based on what they look like on-screen are already in gamma-space and should not be double-converted. Colors calculated using math are often in the linear RGB space.

Read more about gamma-correct rendering here, here, and here.

In versions prior to 11.0, color component values were within the range of 0 to 255 instead of 0 to 1.

love.math.linearToGamma(lr, lg, lb)

| name | type | description |
| --- | --- | --- |
| lr | number | The red channel of the linear RGB color to convert. |
| lg | number | The green channel of the linear RGB color to convert. |
| lb | number | The blue channel of the linear RGB color to convert. |

| name | type | description |
| --- | --- | --- |
| cr | number | The red channel of the converted color in gamma sRGB space. |
| cg | number | The green channel of the converted color in gamma sRGB space. |
| cb | number | The blue channel of the converted color in gamma sRGB space. |

love.math.linearToGamma(color)

| name | type | description |
| --- | --- | --- |
| color | table | An array with the red, green, and blue channels of the linear RGB color to convert. |

| name | type | description |
| --- | --- | --- |
| cr | number | The red channel of the converted color in gamma sRGB space. |
| cg | number | The green channel of the converted color in gamma sRGB space. |
| cb | number | The blue channel of the converted color in gamma sRGB space. |

love.math.linearToGamma(lc)

| name | type | description |
| --- | --- | --- |
| lc | number | The value of a color channel in linear RGB space to convert. |

| name | type | description |
| --- | --- | --- |
| c | number | The value of the color channel in gamma sRGB space. |


love.math.newBezierCurve

Creates a new BezierCurve object.

The number of vertices in the control polygon determines the degree of the curve, e.g. three vertices define a quadratic (degree 2) Bézier curve, four vertices define a cubic (degree 3) Bézier curve, etc.

love.math.newBezierCurve(vertices)

| name | type | description |
| --- | --- | --- |
| vertices | table | The vertices of the control polygon as a table in the form of {x1, y1, x2, y2, x3, y3, ...}. |

| name | type | description |
| --- | --- | --- |
| curve | BezierCurve | A Bézier curve object. |

love.math.newBezierCurve(x1, y1, x2, y2, ...)

| name | type | description |
| --- | --- | --- |
| x1 | number | The position of the first vertex of the control polygon on the x-axis. |
| y1 | number | The position of the first vertex of the control polygon on the y-axis. |
| x2 | number | The position of the second vertex of the control polygon on the x-axis. |
| y2 | number | The position of the second vertex of the control polygon on the y-axis. |
| ... | number | Additional position of the vertex of the control polygon on the x-axis and y-axis. |

| name | type | description |
| --- | --- | --- |
| curve | BezierCurve | A Bézier curve object. |


love.math.newRandomGenerator

Creates a new RandomGenerator object which is completely independent of other RandomGenerator objects and random functions.

love.math.newRandomGenerator()

| name | type | description |
| --- | --- | --- |
| rng | RandomGenerator | The new Random Number Generator object. |

love.math.newRandomGenerator(seed)

| name | type | description |
| --- | --- | --- |
| seed | number | The initial seed number to use for this object. |

| name | type | description |
| --- | --- | --- |
| rng | RandomGenerator | The new Random Number Generator object. |

love.math.newRandomGenerator(low, high)

| name | type | description |
| --- | --- | --- |
| low | number | The lower 32 bits of the seed number to use for this object. |
| high | number | The higher 32 bits of the seed number to use for this object. |

| name | type | description |
| --- | --- | --- |
| rng | RandomGenerator | The new Random Number Generator object. |


love.math.newTransform

Creates a new Transform object.

love.math.newTransform()

| name | type | description |
| --- | --- | --- |
| transform | Transform | The new Transform object. |

love.math.newTransform(x, y, angle, sx, sy, ox, oy, kx, ky)

| name | type | description |
| --- | --- | --- |
| x | number | The position of the new Transform on the x-axis. |
| y | number | The position of the new Transform on the y-axis. |
| angle | number | The orientation of the new Transform in radians. |
| sx | number | Scale factor on the x-axis. |
| sy | number | Scale factor on the y-axis. |
| ox | number | Origin offset on the x-axis. |
| oy | number | Origin offset on the y-axis. |
| kx | number | Shearing / skew factor on the x-axis. |
| ky | number | Shearing / skew factor on the y-axis. |

| name | type | description |
| --- | --- | --- |
| transform | Transform | The new Transform object. |


love.math.noise

Generates a Simplex or Perlin noise value in 1-4 dimensions. The return value will always be the same, given the same arguments.

Simplex noise is closely related to Perlin noise. It is widely used for procedural content generation.

There are many webpages which discuss Perlin and Simplex noise in detail.

love.math.noise(x)

| name | type | description |
| --- | --- | --- |
| x | number | The number used to generate the noise value. |

| name | type | description |
| --- | --- | --- |
| value | number | The noise value in the range of 1. |

love.math.noise(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The first value of the 2-dimensional vector used to generate the noise value. |
| y | number | The second value of the 2-dimensional vector used to generate the noise value. |

| name | type | description |
| --- | --- | --- |
| value | number | The noise value in the range of 1. |

love.math.noise(x, y, z)

| name | type | description |
| --- | --- | --- |
| x | number | The first value of the 3-dimensional vector used to generate the noise value. |
| y | number | The second value of the 3-dimensional vector used to generate the noise value. |
| z | number | The third value of the 3-dimensional vector used to generate the noise value. |

| name | type | description |
| --- | --- | --- |
| value | number | The noise value in the range of 1. |

love.math.noise(x, y, z, w)

| name | type | description |
| --- | --- | --- |
| x | number | The first value of the 4-dimensional vector used to generate the noise value. |
| y | number | The second value of the 4-dimensional vector used to generate the noise value. |
| z | number | The third value of the 4-dimensional vector used to generate the noise value. |
| w | number | The fourth value of the 4-dimensional vector used to generate the noise value. |

| name | type | description |
| --- | --- | --- |
| value | number | The noise value in the range of 1. |


love.math.random

Generates a pseudo-random number in a platform independent manner. The default love.run seeds this function at startup, so you generally don't need to seed it yourself.

love.math.random()

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random number. |

love.math.random(max)

| name | type | description |
| --- | --- | --- |
| max | number | The maximum possible value it should return. |

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random integer number. |

love.math.random(min, max)

| name | type | description |
| --- | --- | --- |
| min | number | The minimum possible value it should return. |
| max | number | The maximum possible value it should return. |

| name | type | description |
| --- | --- | --- |
| number | number | The pseudo-random integer number. |


love.math.randomNormal

Get a normally distributed pseudo random number.

love.math.randomNormal(stddev, mean)

| name | type | description |
| --- | --- | --- |
| stddev | number | Standard deviation of the distribution. |
| mean | number | The mean of the distribution. |

| name | type | description |
| --- | --- | --- |
| number | number | Normally distributed random number with variance (stddev)² and the specified mean. |


love.math.setRandomSeed

Sets the seed of the random number generator using the specified integer number. This is called internally at startup, so you generally don't need to call it yourself.

love.math.setRandomSeed(seed)

| name | type | description |
| --- | --- | --- |
| seed | number | The integer number with which you want to seed the randomization. Must be within the range of 2^53 - 1. |

love.math.setRandomSeed(low, high)

| name | type | description |
| --- | --- | --- |
| low | number | The lower 32 bits of the seed value. Must be within the range of 2^32 - 1. |
| high | number | The higher 32 bits of the seed value. Must be within the range of 2^32 - 1. |


love.math.setRandomState

Sets the current state of the random number generator. The value used as an argument for this function is an opaque implementation-dependent string and should only originate from a previous call to love.math.getRandomState.

This is different from love.math.setRandomSeed in that setRandomState directly sets the random number generator's current implementation-dependent state, whereas setRandomSeed gives it a new seed value.

love.math.setRandomState(state)

| name | type | description |
| --- | --- | --- |
| state | string | The new state of the random number generator, represented as a string. This should originate from a previous call to love.math.getRandomState. |


love.math.triangulate

Decomposes a simple convex or concave polygon into triangles.

love.math.triangulate(polygon)

| name | type | description |
| --- | --- | --- |
| polygon | table | Polygon to triangulate. Must not intersect itself. |

| name | type | description |
| --- | --- | --- |
| triangles | table | List of triangles the polygon is composed of, in the form of {{x1, y1, x2, y2, x3, y3},  {x1, y1, x2, y2, x3, y3}, ...}. |

love.math.triangulate(x1, y1, x2, y2, x3, y3)

| name | type | description |
| --- | --- | --- |
| x1 | number | The position of the first vertex of the polygon on the x-axis. |
| y1 | number | The position of the first vertex of the polygon on the y-axis. |
| x2 | number | The position of the second vertex of the polygon on the x-axis. |
| y2 | number | The position of the second vertex of the polygon on the y-axis. |
| x3 | number | The position of the third vertex of the polygon on the x-axis. |
| y3 | number | The position of the third vertex of the polygon on the y-axis. |

| name | type | description |
| --- | --- | --- |
| triangles | table | List of triangles the polygon is composed of, in the form of {{x1, y1, x2, y2, x3, y3},  {x1, y1, x2, y2, x3, y3}, ...}. |


love.mouse.getCursor

Gets the current Cursor.

love.mouse.getCursor()

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The current cursor, or nil if no cursor is set. |


love.mouse.getPosition

Returns the current position of the mouse.

love.mouse.getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | The position of the mouse along the x-axis. |
| y | number | The position of the mouse along the y-axis. |


love.mouse.getRelativeMode

Gets whether relative mode is enabled for the mouse.

If relative mode is enabled, the cursor is hidden and doesn't move when the mouse does, but relative mouse motion events are still generated via love.mousemoved. This lets the mouse move in any direction indefinitely without the cursor getting stuck at the edges of the screen.

The reported position of the mouse is not updated while relative mode is enabled, even when relative mouse motion events are generated.

love.mouse.getRelativeMode()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if relative mode is enabled, false if it's disabled. |


love.mouse.getSystemCursor

Gets a Cursor object representing a system-native hardware cursor.

Hardware cursors are framerate-independent and work the same way as normal operating system cursors. Unlike drawing an image at the mouse's current coordinates, hardware cursors never have visible lag between when the mouse is moved and when the cursor position updates, even at low framerates.

love.mouse.getSystemCursor(ctype)

| name | type | description |
| --- | --- | --- |
| ctype | CursorType | The type of system cursor to get. |

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The Cursor object representing the system cursor type. |


love.mouse.getX

Returns the current x-position of the mouse.

love.mouse.getX()

| name | type | description |
| --- | --- | --- |
| x | number | The position of the mouse along the x-axis. |


love.mouse.getY

Returns the current y-position of the mouse.

love.mouse.getY()

| name | type | description |
| --- | --- | --- |
| y | number | The position of the mouse along the y-axis. |


love.mouse.isCursorSupported

Gets whether cursor functionality is supported.

If it isn't supported, calling love.mouse.newCursor and love.mouse.getSystemCursor will cause an error. Mobile devices do not support cursors.

love.mouse.isCursorSupported()

| name | type | description |
| --- | --- | --- |
| supported | boolean | Whether the system has cursor functionality. |


love.mouse.isDown

Checks whether a certain mouse button is down.

This function does not detect mouse wheel scrolling; you must use the love.wheelmoved (or love.mousepressed in version 0.9.2 and older) callback for that.

love.mouse.isDown(button, ...)

| name | type | description |
| --- | --- | --- |
| button | number | The index of a button to check. 1 is the primary mouse button, 2 is the secondary mouse button and 3 is the middle button. Further buttons are mouse dependant. |
| ... | number | Additional button numbers to check. |

| name | type | description |
| --- | --- | --- |
| down | boolean | True if any specified button is down. |


love.mouse.isGrabbed

Checks if the mouse is grabbed.

love.mouse.isGrabbed()

| name | type | description |
| --- | --- | --- |
| grabbed | boolean | True if the cursor is grabbed, false if it is not. |


love.mouse.isVisible

Checks if the cursor is visible.

love.mouse.isVisible()

| name | type | description |
| --- | --- | --- |
| visible | boolean | True if the cursor to visible, false if the cursor is hidden. |


love.mouse.newCursor

Creates a new hardware Cursor object from an image file or ImageData.

Hardware cursors are framerate-independent and work the same way as normal operating system cursors. Unlike drawing an image at the mouse's current coordinates, hardware cursors never have visible lag between when the mouse is moved and when the cursor position updates, even at low framerates.

The hot spot is the point the operating system uses to determine what was clicked and at what position the mouse cursor is. For example, the normal arrow pointer normally has its hot spot at the top left of the image, but a crosshair cursor might have it in the middle.

love.mouse.newCursor(imageData, hotx, hoty)

| name | type | description |
| --- | --- | --- |
| imageData | ImageData | The ImageData to use for the new Cursor. |
| hotx | number | The x-coordinate in the ImageData of the cursor's hot spot. |
| hoty | number | The y-coordinate in the ImageData of the cursor's hot spot. |

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The new Cursor object. |

love.mouse.newCursor(filename, hotx, hoty)

| name | type | description |
| --- | --- | --- |
| filename | string | Path to the image to use for the new Cursor. |
| hotx | number | The x-coordinate in the image of the cursor's hot spot. |
| hoty | number | The y-coordinate in the image of the cursor's hot spot. |

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The new Cursor object. |

love.mouse.newCursor(fileData, hotx, hoty)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | Data representing the image to use for the new Cursor. |
| hotx | number | The x-coordinate in the image of the cursor's hot spot. |
| hoty | number | The y-coordinate in the image of the cursor's hot spot. |

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The new Cursor object. |


love.mouse.setCursor

Sets the current mouse cursor.

love.mouse.setCursor(cursor)

| name | type | description |
| --- | --- | --- |
| cursor | Cursor | The Cursor object to use as the current mouse cursor. |

love.mouse.setCursor()


love.mouse.setGrabbed

Grabs the mouse and confines it to the window.

love.mouse.setGrabbed(grab)

| name | type | description |
| --- | --- | --- |
| grab | boolean | True to confine the mouse, false to let it leave the window. |


love.mouse.setPosition

Sets the current position of the mouse. Non-integer values are floored.

love.mouse.setPosition(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The new position of the mouse along the x-axis. |
| y | number | The new position of the mouse along the y-axis. |


love.mouse.setRelativeMode

Sets whether relative mode is enabled for the mouse.

When relative mode is enabled, the cursor is hidden and doesn't move when the mouse does, but relative mouse motion events are still generated via love.mousemoved. This lets the mouse move in any direction indefinitely without the cursor getting stuck at the edges of the screen.

The reported position of the mouse may not be updated while relative mode is enabled, even when relative mouse motion events are generated.

love.mouse.setRelativeMode(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable relative mode, false to disable it. |


love.mouse.setVisible

Sets the current visibility of the cursor.

love.mouse.setVisible(visible)

| name | type | description |
| --- | --- | --- |
| visible | boolean | True to set the cursor to visible, false to hide the cursor. |


love.mouse.setX

Sets the current X position of the mouse.

Non-integer values are floored.

love.mouse.setX(x)

| name | type | description |
| --- | --- | --- |
| x | number | The new position of the mouse along the x-axis. |


love.mouse.setY

Sets the current Y position of the mouse.

Non-integer values are floored.

love.mouse.setY(y)

| name | type | description |
| --- | --- | --- |
| y | number | The new position of the mouse along the y-axis. |


love.mousefocus

Callback function triggered when window receives or loses mouse focus.

love.mousefocus(focus)

| name | type | description |
| --- | --- | --- |
| focus | boolean | Whether the window has mouse focus or not. |


love.mousemoved

Callback function triggered when the mouse is moved.

love.mousemoved(x, y, dx, dy, istouch)

| name | type | description |
| --- | --- | --- |
| x | number | The mouse position on the x-axis. |
| y | number | The mouse position on the y-axis. |
| dx | number | The amount moved along the x-axis since the last time love.mousemoved was called. |
| dy | number | The amount moved along the y-axis since the last time love.mousemoved was called. |
| istouch | boolean | True if the mouse button press originated from a touchscreen touch-press. |


love.mousepressed

Callback function triggered when a mouse button is pressed.

love.mousepressed(x, y, button, istouch, presses)

| name | type | description |
| --- | --- | --- |
| x | number | Mouse x position, in pixels. |
| y | number | Mouse y position, in pixels. |
| button | number | The button index that was pressed. 1 is the primary mouse button, 2 is the secondary mouse button and 3 is the middle button. Further buttons are mouse dependent. |
| istouch | boolean | True if the mouse button press originated from a touchscreen touch-press. |
| presses | number | The number of presses in a short time frame and small area, used to simulate double, triple clicks |


love.mousereleased

Callback function triggered when a mouse button is released.

love.mousereleased(x, y, button, istouch, presses)

| name | type | description |
| --- | --- | --- |
| x | number | Mouse x position, in pixels. |
| y | number | Mouse y position, in pixels. |
| button | number | The button index that was released. 1 is the primary mouse button, 2 is the secondary mouse button and 3 is the middle button. Further buttons are mouse dependent. |
| istouch | boolean | True if the mouse button release originated from a touchscreen touch-release. |
| presses | number | The number of presses in a short time frame and small area, used to simulate double, triple clicks |


love.physics.getDistance

Returns the two closest points between two fixtures and their distance.

love.physics.getDistance(fixture1, fixture2)

| name | type | description |
| --- | --- | --- |
| fixture1 | Fixture | The first fixture. |
| fixture2 | Fixture | The second fixture. |

| name | type | description |
| --- | --- | --- |
| distance | number | The distance of the two points. |
| x1 | number | The x-coordinate of the first point. |
| y1 | number | The y-coordinate of the first point. |
| x2 | number | The x-coordinate of the second point. |
| y2 | number | The y-coordinate of the second point. |


love.physics.getMeter

Returns the meter scale factor.

All coordinates in the physics module are divided by this number, creating a convenient way to draw the objects directly to the screen without the need for graphics transformations.

It is recommended to create shapes no larger than 10 times the scale. This is important because Box2D is tuned to work well with shape sizes from 0.1 to 10 meters.

love.physics.getMeter()

| name | type | description |
| --- | --- | --- |
| scale | number | The scale factor as an integer. |


love.physics.newBody

Creates a new body.

There are three types of bodies.

* Static bodies do not move, have a infinite mass, and can be used for level boundaries.

* Dynamic bodies are the main actors in the simulation, they collide with everything.

* Kinematic bodies do not react to forces and only collide with dynamic bodies.

The mass of the body gets calculated when a Fixture is attached or removed, but can be changed at any time with Body:setMass or Body:resetMassData.

love.physics.newBody(world, x, y, type)

| name | type | description |
| --- | --- | --- |
| world | World | The world to create the body in. |
| x | number | The x position of the body. |
| y | number | The y position of the body. |
| type | BodyType | The type of the body. |

| name | type | description |
| --- | --- | --- |
| body | Body | A new body. |


love.physics.newChainShape

Creates a new ChainShape.

love.physics.newChainShape(loop, x1, y1, x2, y2, ...)

| name | type | description |
| --- | --- | --- |
| loop | boolean | If the chain should loop back to the first point. |
| x1 | number | The x position of the first point. |
| y1 | number | The y position of the first point. |
| x2 | number | The x position of the second point. |
| y2 | number | The y position of the second point. |
| ... | number | Additional point positions. |

| name | type | description |
| --- | --- | --- |
| shape | ChainShape | The new shape. |

love.physics.newChainShape(loop, points)

| name | type | description |
| --- | --- | --- |
| loop | boolean | If the chain should loop back to the first point. |
| points | table | A list of points to construct the ChainShape, in the form of {x1, y1, x2, y2, ...}. |

| name | type | description |
| --- | --- | --- |
| shape | ChainShape | The new shape. |


love.physics.newCircleShape

Creates a new CircleShape.

love.physics.newCircleShape(radius)

| name | type | description |
| --- | --- | --- |
| radius | number | The radius of the circle. |

| name | type | description |
| --- | --- | --- |
| shape | CircleShape | The new shape. |

love.physics.newCircleShape(x, y, radius)

| name | type | description |
| --- | --- | --- |
| x | number | The x position of the circle. |
| y | number | The y position of the circle. |
| radius | number | The radius of the circle. |

| name | type | description |
| --- | --- | --- |
| shape | CircleShape | The new shape. |


love.physics.newDistanceJoint

Creates a DistanceJoint between two bodies.

This joint constrains the distance between two points on two bodies to be constant. These two points are specified in world coordinates and the two bodies are assumed to be in place when this joint is created. The first anchor point is connected to the first body and the second to the second body, and the points define the length of the distance joint.

love.physics.newDistanceJoint(body1, body2, x1, y1, x2, y2, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x1 | number | The x position of the first anchor point (world space). |
| y1 | number | The y position of the first anchor point (world space). |
| x2 | number | The x position of the second anchor point (world space). |
| y2 | number | The y position of the second anchor point (world space). |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | DistanceJoint | The new distance joint. |


love.physics.newEdgeShape

Creates a new EdgeShape.

love.physics.newEdgeShape(x1, y1, x2, y2)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the first point. |
| y1 | number | The y position of the first point. |
| x2 | number | The x position of the second point. |
| y2 | number | The y position of the second point. |

| name | type | description |
| --- | --- | --- |
| shape | EdgeShape | The new shape. |


love.physics.newFixture

Creates and attaches a Fixture to a body.

Note that the Shape object is copied rather than kept as a reference when the Fixture is created. To get the Shape object that the Fixture owns, use Fixture:getShape.

love.physics.newFixture(body, shape, density)

| name | type | description |
| --- | --- | --- |
| body | Body | The body which gets the fixture attached. |
| shape | Shape | The shape to be copied to the fixture. |
| density | number | The density of the fixture. |

| name | type | description |
| --- | --- | --- |
| fixture | Fixture | The new fixture. |


love.physics.newFrictionJoint

Create a friction joint between two bodies. A FrictionJoint applies friction to a body.

love.physics.newFrictionJoint(body1, body2, x, y, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x | number | The x position of the anchor point. |
| y | number | The y position of the anchor point. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | FrictionJoint | The new FrictionJoint. |

love.physics.newFrictionJoint(body1, body2, x1, y1, x2, y2, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x1 | number | The x position of the first anchor point. |
| y1 | number | The y position of the first anchor point. |
| x2 | number | The x position of the second anchor point. |
| y2 | number | The y position of the second anchor point. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | FrictionJoint | The new FrictionJoint. |


love.physics.newGearJoint

Create a GearJoint connecting two Joints.

The gear joint connects two joints that must be either  prismatic or  revolute joints. Using this joint requires that the joints it uses connect their respective bodies to the ground and have the ground as the first body. When destroying the bodies and joints you must make sure you destroy the gear joint before the other joints.

The gear joint has a ratio the determines how the angular or distance values of the connected joints relate to each other. The formula coordinate1 + ratio * coordinate2 always has a constant value that is set when the gear joint is created.

love.physics.newGearJoint(joint1, joint2, ratio, collideConnected)

| name | type | description |
| --- | --- | --- |
| joint1 | Joint | The first joint to connect with a gear joint. |
| joint2 | Joint | The second joint to connect with a gear joint. |
| ratio | number | The gear ratio. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | GearJoint | The new gear joint. |


love.physics.newMotorJoint

Creates a joint between two bodies which controls the relative motion between them.

Position and rotation offsets can be specified once the MotorJoint has been created, as well as the maximum motor force and torque that will be be applied to reach the target offsets.

love.physics.newMotorJoint(body1, body2, correctionFactor)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| correctionFactor | number | The joint's initial position correction factor, in the range of 1. |

| name | type | description |
| --- | --- | --- |
| joint | MotorJoint | The new MotorJoint. |

love.physics.newMotorJoint(body1, body2, correctionFactor, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| correctionFactor | number | The joint's initial position correction factor, in the range of 1. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | MotorJoint | The new MotorJoint. |


love.physics.newMouseJoint

Create a joint between a body and the mouse.

This joint actually connects the body to a fixed point in the world. To make it follow the mouse, the fixed point must be updated every timestep (example below).

The advantage of using a MouseJoint instead of just changing a body position directly is that collisions and reactions to other joints are handled by the physics engine.

love.physics.newMouseJoint(body, x, y)

| name | type | description |
| --- | --- | --- |
| body | Body | The body to attach to the mouse. |
| x | number | The x position of the connecting point. |
| y | number | The y position of the connecting point. |

| name | type | description |
| --- | --- | --- |
| joint | MouseJoint | The new mouse joint. |


love.physics.newPolygonShape

Creates a new PolygonShape.

This shape can have 8 vertices at most, and must form a convex shape.

love.physics.newPolygonShape(x1, y1, x2, y2, x3, y3, ...)

| name | type | description |
| --- | --- | --- |
| x1 | number | The x position of the first point. |
| y1 | number | The y position of the first point. |
| x2 | number | The x position of the second point. |
| y2 | number | The y position of the second point. |
| x3 | number | The x position of the third point. |
| y3 | number | The y position of the third point. |
| ... | number | You can continue passing more point positions to create the PolygonShape. |

| name | type | description |
| --- | --- | --- |
| shape | PolygonShape | A new PolygonShape. |

love.physics.newPolygonShape(vertices)

| name | type | description |
| --- | --- | --- |
| vertices | table | A list of vertices to construct the polygon, in the form of {x1, y1, x2, y2, x3, y3, ...}. |

| name | type | description |
| --- | --- | --- |
| shape | PolygonShape | A new PolygonShape. |


love.physics.newPrismaticJoint

Creates a PrismaticJoint between two bodies.

A prismatic joint constrains two bodies to move relatively to each other on a specified axis. It does not allow for relative rotation. Its definition and operation are similar to a  revolute joint, but with translation and force substituted for angle and torque.

love.physics.newPrismaticJoint(body1, body2, x, y, ax, ay, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to connect with a prismatic joint. |
| body2 | Body | The second body to connect with a prismatic joint. |
| x | number | The x coordinate of the anchor point. |
| y | number | The y coordinate of the anchor point. |
| ax | number | The x coordinate of the axis vector. |
| ay | number | The y coordinate of the axis vector. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | PrismaticJoint | The new prismatic joint. |

love.physics.newPrismaticJoint(body1, body2, x1, y1, x2, y2, ax, ay, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to connect with a prismatic joint. |
| body2 | Body | The second body to connect with a prismatic joint. |
| x1 | number | The x coordinate of the first anchor point. |
| y1 | number | The y coordinate of the first anchor point. |
| x2 | number | The x coordinate of the second anchor point. |
| y2 | number | The y coordinate of the second anchor point. |
| ax | number | The x coordinate of the axis unit vector. |
| ay | number | The y coordinate of the axis unit vector. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | PrismaticJoint | The new prismatic joint. |

love.physics.newPrismaticJoint(body1, body2, x1, y1, x2, y2, ax, ay, collideConnected, referenceAngle)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to connect with a prismatic joint. |
| body2 | Body | The second body to connect with a prismatic joint. |
| x1 | number | The x coordinate of the first anchor point. |
| y1 | number | The y coordinate of the first anchor point. |
| x2 | number | The x coordinate of the second anchor point. |
| y2 | number | The y coordinate of the second anchor point. |
| ax | number | The x coordinate of the axis unit vector. |
| ay | number | The y coordinate of the axis unit vector. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |
| referenceAngle | number | The reference angle between body1 and body2, in radians. |

| name | type | description |
| --- | --- | --- |
| joint | PrismaticJoint | The new prismatic joint. |


love.physics.newPulleyJoint

Creates a PulleyJoint to join two bodies to each other and the ground.

The pulley joint simulates a pulley with an optional block and tackle. If the ratio parameter has a value different from one, then the simulated rope extends faster on one side than the other. In a pulley joint the total length of the simulated rope is the constant length1 + ratio * length2, which is set when the pulley joint is created.

Pulley joints can behave unpredictably if one side is fully extended. It is recommended that the method  setMaxLengths  be used to constrain the maximum lengths each side can attain.

love.physics.newPulleyJoint(body1, body2, gx1, gy1, gx2, gy2, x1, y1, x2, y2, ratio, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to connect with a pulley joint. |
| body2 | Body | The second body to connect with a pulley joint. |
| gx1 | number | The x coordinate of the first body's ground anchor. |
| gy1 | number | The y coordinate of the first body's ground anchor. |
| gx2 | number | The x coordinate of the second body's ground anchor. |
| gy2 | number | The y coordinate of the second body's ground anchor. |
| x1 | number | The x coordinate of the pulley joint anchor in the first body. |
| y1 | number | The y coordinate of the pulley joint anchor in the first body. |
| x2 | number | The x coordinate of the pulley joint anchor in the second body. |
| y2 | number | The y coordinate of the pulley joint anchor in the second body. |
| ratio | number | The joint ratio. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | PulleyJoint | The new pulley joint. |


love.physics.newRectangleShape

Shorthand for creating rectangular PolygonShapes.

By default, the local origin is located at the '''center''' of the rectangle as opposed to the top left for graphics.

love.physics.newRectangleShape(width, height)

| name | type | description |
| --- | --- | --- |
| width | number | The width of the rectangle. |
| height | number | The height of the rectangle. |

| name | type | description |
| --- | --- | --- |
| shape | PolygonShape | A new PolygonShape. |

love.physics.newRectangleShape(x, y, width, height, angle)

| name | type | description |
| --- | --- | --- |
| x | number | The offset along the x-axis. |
| y | number | The offset along the y-axis. |
| width | number | The width of the rectangle. |
| height | number | The height of the rectangle. |
| angle | number | The initial angle of the rectangle. |

| name | type | description |
| --- | --- | --- |
| shape | PolygonShape | A new PolygonShape. |


love.physics.newRevoluteJoint

Creates a pivot joint between two bodies.

This joint connects two bodies to a point around which they can pivot.

love.physics.newRevoluteJoint(body1, body2, x, y, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body. |
| body2 | Body | The second body. |
| x | number | The x position of the connecting point. |
| y | number | The y position of the connecting point. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | RevoluteJoint | The new revolute joint. |

love.physics.newRevoluteJoint(body1, body2, x1, y1, x2, y2, collideConnected, referenceAngle)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body. |
| body2 | Body | The second body. |
| x1 | number | The x position of the first connecting point. |
| y1 | number | The y position of the first connecting point. |
| x2 | number | The x position of the second connecting point. |
| y2 | number | The y position of the second connecting point. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |
| referenceAngle | number | The reference angle between body1 and body2, in radians. |

| name | type | description |
| --- | --- | --- |
| joint | RevoluteJoint | The new revolute joint. |


love.physics.newRopeJoint

Creates a joint between two bodies. Its only function is enforcing a max distance between these bodies.

love.physics.newRopeJoint(body1, body2, x1, y1, x2, y2, maxLength, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x1 | number | The x position of the first anchor point. |
| y1 | number | The y position of the first anchor point. |
| x2 | number | The x position of the second anchor point. |
| y2 | number | The y position of the second anchor point. |
| maxLength | number | The maximum distance for the bodies. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | RopeJoint | The new RopeJoint. |


love.physics.newWeldJoint

Creates a constraint joint between two bodies. A WeldJoint essentially glues two bodies together. The constraint is a bit soft, however, due to Box2D's iterative solver.

love.physics.newWeldJoint(body1, body2, x, y, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x | number | The x position of the anchor point (world space). |
| y | number | The y position of the anchor point (world space). |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | WeldJoint | The new WeldJoint. |

love.physics.newWeldJoint(body1, body2, x1, y1, x2, y2, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x1 | number | The x position of the first anchor point (world space). |
| y1 | number | The y position of the first anchor point (world space). |
| x2 | number | The x position of the second anchor point (world space). |
| y2 | number | The y position of the second anchor point (world space). |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | WeldJoint | The new WeldJoint. |

love.physics.newWeldJoint(body1, body2, x1, y1, x2, y2, collideConnected, referenceAngle)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body to attach to the joint. |
| body2 | Body | The second body to attach to the joint. |
| x1 | number | The x position of the first anchor point (world space). |
| y1 | number | The y position of the first anchor point  (world space). |
| x2 | number | The x position of the second anchor point (world space). |
| y2 | number | The y position of the second anchor point (world space). |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |
| referenceAngle | number | The reference angle between body1 and body2, in radians. |

| name | type | description |
| --- | --- | --- |
| joint | WeldJoint | The new WeldJoint. |


love.physics.newWheelJoint

Creates a wheel joint.

love.physics.newWheelJoint(body1, body2, x, y, ax, ay, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body. |
| body2 | Body | The second body. |
| x | number | The x position of the anchor point. |
| y | number | The y position of the anchor point. |
| ax | number | The x position of the axis unit vector. |
| ay | number | The y position of the axis unit vector. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | WheelJoint | The new WheelJoint. |

love.physics.newWheelJoint(body1, body2, x1, y1, x2, y2, ax, ay, collideConnected)

| name | type | description |
| --- | --- | --- |
| body1 | Body | The first body. |
| body2 | Body | The second body. |
| x1 | number | The x position of the first anchor point. |
| y1 | number | The y position of the first anchor point. |
| x2 | number | The x position of the second anchor point. |
| y2 | number | The y position of the second anchor point. |
| ax | number | The x position of the axis unit vector. |
| ay | number | The y position of the axis unit vector. |
| collideConnected | boolean | Specifies whether the two bodies should collide with each other. |

| name | type | description |
| --- | --- | --- |
| joint | WheelJoint | The new WheelJoint. |


love.physics.newWorld

Creates a new World.

love.physics.newWorld(xg, yg, sleep)

| name | type | description |
| --- | --- | --- |
| xg | number | The x component of gravity. |
| yg | number | The y component of gravity. |
| sleep | boolean | Whether the bodies in this world are allowed to sleep. |

| name | type | description |
| --- | --- | --- |
| world | World | A brave new World. |


love.physics.setMeter

Sets the pixels to meter scale factor.

All coordinates in the physics module are divided by this number and converted to meters, and it creates a convenient way to draw the objects directly to the screen without the need for graphics transformations.

It is recommended to create shapes no larger than 10 times the scale. This is important because Box2D is tuned to work well with shape sizes from 0.1 to 10 meters. The default meter scale is 30.

love.physics.setMeter(scale)

| name | type | description |
| --- | --- | --- |
| scale | number | The scale factor as an integer. |


love.quit

Callback function triggered when the game is closed.

love.quit()

| name | type | description |
| --- | --- | --- |
| r | boolean | Abort quitting. If true, do not close the game. |


love.resize

Called when the window is resized, for example if the user resizes the window, or if love.window.setMode is called with an unsupported width or height in fullscreen and the window chooses the closest appropriate size.

love.resize(w, h)

| name | type | description |
| --- | --- | --- |
| w | number | The new width. |
| h | number | The new height. |


love.run

The main function, containing the main loop. A sensible default is used when left out.

love.run()

| name | type | description |
| --- | --- | --- |
| mainLoop | function | Function which handlers one frame, including events and rendering when called. |


love.setDeprecationOutput

Sets whether LÖVE displays warnings when using deprecated functionality. It is disabled by default in fused mode, and enabled by default otherwise.

When deprecation output is enabled, the first use of a formally deprecated LÖVE API will show a message at the bottom of the screen for a short time, and print the message to the console.

love.setDeprecationOutput(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | Whether to enable or disable deprecation output. |


love.sound.newDecoder

Attempts to find a decoder for the encoded sound data in the specified file.

love.sound.newDecoder(file, buffer)

| name | type | description |
| --- | --- | --- |
| file | File | The file with encoded sound data. |
| buffer | number | The size of each decoded chunk, in bytes. |

| name | type | description |
| --- | --- | --- |
| decoder | Decoder | A new Decoder object. |

love.sound.newDecoder(filename, buffer)

| name | type | description |
| --- | --- | --- |
| filename | string | The filename of the file with encoded sound data. |
| buffer | number | The size of each decoded chunk, in bytes. |

| name | type | description |
| --- | --- | --- |
| decoder | Decoder | A new Decoder object. |


love.sound.newSoundData

Creates new SoundData from a filepath, File, or Decoder. It's also possible to create SoundData with a custom sample rate, channel and bit depth.

The sound data will be decoded to the memory in a raw format. It is recommended to create only short sounds like effects, as a 3 minute song uses 30 MB of memory this way.

love.sound.newSoundData(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The file name of the file to load. |

| name | type | description |
| --- | --- | --- |
| soundData | SoundData | A new SoundData object. |

love.sound.newSoundData(file)

| name | type | description |
| --- | --- | --- |
| file | File | A File pointing to an audio file. |

| name | type | description |
| --- | --- | --- |
| soundData | SoundData | A new SoundData object. |

love.sound.newSoundData(decoder)

| name | type | description |
| --- | --- | --- |
| decoder | Decoder | Decode data from this Decoder until EOF. |

| name | type | description |
| --- | --- | --- |
| soundData | SoundData | A new SoundData object. |

love.sound.newSoundData(samples, rate, bits, channels)

| name | type | description |
| --- | --- | --- |
| samples | number | Total number of samples. |
| rate | number | Number of samples per second |
| bits | number | Bits per sample (8 or 16). |
| channels | number | Either 1 for mono or 2 for stereo. |

| name | type | description |
| --- | --- | --- |
| soundData | SoundData | A new SoundData object. |


love.system.getClipboardText

Gets text from the clipboard.

love.system.getClipboardText()

| name | type | description |
| --- | --- | --- |
| text | string | The text currently held in the system's clipboard. |


love.system.getOS

Gets the current operating system. In general, LÖVE abstracts away the need to know the current operating system, but there are a few cases where it can be useful (especially in combination with os.execute.)

love.system.getOS()

| name | type | description |
| --- | --- | --- |
| osString | string | The current operating system. 'OS X', 'Windows', 'Linux', 'Android' or 'iOS'. |


love.system.getPowerInfo

Gets information about the system's power supply.

love.system.getPowerInfo()

| name | type | description |
| --- | --- | --- |
| state | PowerState | The basic state of the power supply. |
| percent | number | Percentage of battery life left, between 0 and 100. nil if the value can't be determined or there's no battery. |
| seconds | number | Seconds of battery life left. nil if the value can't be determined or there's no battery. |


love.system.getProcessorCount

Gets the amount of logical processor in the system.

love.system.getProcessorCount()

| name | type | description |
| --- | --- | --- |
| processorCount | number | Amount of logical processors. |


love.system.hasBackgroundMusic

Gets whether another application on the system is playing music in the background.

Currently this is implemented on iOS and Android, and will always return false on other operating systems. The t.audio.mixwithsystem flag in love.conf can be used to configure whether background audio / music from other apps should play while LÖVE is open.

love.system.hasBackgroundMusic()

| name | type | description |
| --- | --- | --- |
| backgroundmusic | boolean | True if the user is playing music in the background via another app, false otherwise. |


love.system.openURL

Opens a URL with the user's web or file browser.

love.system.openURL(url)

| name | type | description |
| --- | --- | --- |
| url | string | The URL to open. Must be formatted as a proper URL. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the URL was opened successfully. |


love.system.setClipboardText

Puts text in the clipboard.

love.system.setClipboardText(text)

| name | type | description |
| --- | --- | --- |
| text | string | The new text to hold in the system's clipboard. |


love.system.vibrate

Causes the device to vibrate, if possible. Currently this will only work on Android and iOS devices that have a built-in vibration motor.

love.system.vibrate(seconds)

| name | type | description |
| --- | --- | --- |
| seconds | number | The duration to vibrate for. If called on an iOS device, it will always vibrate for 0.5 seconds due to limitations in the iOS system APIs. |


love.textedited

Called when the candidate text for an IME (Input Method Editor) has changed.

The candidate text is not the final text that the user will eventually choose. Use love.textinput for that.

love.textedited(text, start, length)

| name | type | description |
| --- | --- | --- |
| text | string | The UTF-8 encoded unicode candidate text. |
| start | number | The start cursor of the selected candidate text. |
| length | number | The length of the selected candidate text. May be 0. |


love.textinput

Called when text has been entered by the user. For example if shift-2 is pressed on an American keyboard layout, the text '@' will be generated.

love.textinput(text)

| name | type | description |
| --- | --- | --- |
| text | string | The UTF-8 encoded unicode text. |


love.thread.getChannel

Creates or retrieves a named thread channel.

love.thread.getChannel(name)

| name | type | description |
| --- | --- | --- |
| name | string | The name of the channel you want to create or retrieve. |

| name | type | description |
| --- | --- | --- |
| channel | Channel | The Channel object associated with the name. |


love.thread.newChannel

Create a new unnamed thread channel.

One use for them is to pass new unnamed channels to other threads via Channel:push on a named channel.

love.thread.newChannel()

| name | type | description |
| --- | --- | --- |
| channel | Channel | The new Channel object. |


love.thread.newThread

Creates a new Thread from a filename, string or FileData object containing Lua code.

love.thread.newThread(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The name of the Lua file to use as the source. |

| name | type | description |
| --- | --- | --- |
| thread | Thread | A new Thread that has yet to be started. |

love.thread.newThread(fileData)

| name | type | description |
| --- | --- | --- |
| fileData | FileData | The FileData containing the Lua code to use as the source. |

| name | type | description |
| --- | --- | --- |
| thread | Thread | A new Thread that has yet to be started. |

love.thread.newThread(codestring)

| name | type | description |
| --- | --- | --- |
| codestring | string | A string containing the Lua code to use as the source. It needs to either be at least 1024 characters long, or contain at least one newline. |

| name | type | description |
| --- | --- | --- |
| thread | Thread | A new Thread that has yet to be started. |


love.threaderror

Callback function triggered when a Thread encounters an error.

love.threaderror(thread, errorstr)

| name | type | description |
| --- | --- | --- |
| thread | Thread | The thread which produced the error. |
| errorstr | string | The error message. |


love.timer.getAverageDelta

Returns the average delta time (seconds per frame) over the last second.

love.timer.getAverageDelta()

| name | type | description |
| --- | --- | --- |
| delta | number | The average delta time over the last second. |


love.timer.getDelta

Returns the time between the last two frames.

love.timer.getDelta()

| name | type | description |
| --- | --- | --- |
| dt | number | The time passed (in seconds). |


love.timer.getFPS

Returns the current frames per second.

love.timer.getFPS()

| name | type | description |
| --- | --- | --- |
| fps | number | The current FPS. |


love.timer.getTime

Returns the value of a timer with an unspecified starting time.

This function should only be used to calculate differences between points in time, as the starting time of the timer is unknown.

love.timer.getTime()

| name | type | description |
| --- | --- | --- |
| time | number | The time in seconds. Given as a decimal, accurate to the microsecond. |


love.timer.sleep

Pauses the current thread for the specified amount of time.

love.timer.sleep(s)

| name | type | description |
| --- | --- | --- |
| s | number | Seconds to sleep for. |


love.timer.step

Measures the time between two frames.

Calling this changes the return value of love.timer.getDelta.

love.timer.step()

| name | type | description |
| --- | --- | --- |
| dt | number | The time passed (in seconds). |


love.touch.getPosition

Gets the current position of the specified touch-press, in pixels.

love.touch.getPosition(id)

| name | type | description |
| --- | --- | --- |
| id | light userdata | The identifier of the touch-press. Use love.touch.getTouches, love.touchpressed, or love.touchmoved to obtain touch id values. |

| name | type | description |
| --- | --- | --- |
| x | number | The position along the x-axis of the touch-press inside the window, in pixels. |
| y | number | The position along the y-axis of the touch-press inside the window, in pixels. |


love.touch.getPressure

Gets the current pressure of the specified touch-press.

love.touch.getPressure(id)

| name | type | description |
| --- | --- | --- |
| id | light userdata | The identifier of the touch-press. Use love.touch.getTouches, love.touchpressed, or love.touchmoved to obtain touch id values. |

| name | type | description |
| --- | --- | --- |
| pressure | number | The pressure of the touch-press. Most touch screens aren't pressure sensitive, in which case the pressure will be 1. |


love.touch.getTouches

Gets a list of all active touch-presses.

love.touch.getTouches()

| name | type | description |
| --- | --- | --- |
| touches | table | A list of active touch-press id values, which can be used with love.touch.getPosition. |


love.touchmoved

Callback function triggered when a touch press moves inside the touch screen.

love.touchmoved(id, x, y, dx, dy, pressure)

| name | type | description |
| --- | --- | --- |
| id | light userdata | The identifier for the touch press. |
| x | number | The x-axis position of the touch inside the window, in pixels. |
| y | number | The y-axis position of the touch inside the window, in pixels. |
| dx | number | The x-axis movement of the touch inside the window, in pixels. |
| dy | number | The y-axis movement of the touch inside the window, in pixels. |
| pressure | number | The amount of pressure being applied. Most touch screens aren't pressure sensitive, in which case the pressure will be 1. |


love.touchpressed

Callback function triggered when the touch screen is touched.

love.touchpressed(id, x, y, dx, dy, pressure)

| name | type | description |
| --- | --- | --- |
| id | light userdata | The identifier for the touch press. |
| x | number | The x-axis position of the touch press inside the window, in pixels. |
| y | number | The y-axis position of the touch press inside the window, in pixels. |
| dx | number | The x-axis movement of the touch press inside the window, in pixels. This should always be zero. |
| dy | number | The y-axis movement of the touch press inside the window, in pixels. This should always be zero. |
| pressure | number | The amount of pressure being applied. Most touch screens aren't pressure sensitive, in which case the pressure will be 1. |


love.touchreleased

Callback function triggered when the touch screen stops being touched.

love.touchreleased(id, x, y, dx, dy, pressure)

| name | type | description |
| --- | --- | --- |
| id | light userdata | The identifier for the touch press. |
| x | number | The x-axis position of the touch inside the window, in pixels. |
| y | number | The y-axis position of the touch inside the window, in pixels. |
| dx | number | The x-axis movement of the touch inside the window, in pixels. |
| dy | number | The y-axis movement of the touch inside the window, in pixels. |
| pressure | number | The amount of pressure being applied. Most touch screens aren't pressure sensitive, in which case the pressure will be 1. |


love.update

Callback function used to update the state of the game every frame.

love.update(dt)

| name | type | description |
| --- | --- | --- |
| dt | number | Time since the last update in seconds. |


love.video.newVideoStream

Creates a new VideoStream. Currently only Ogg Theora video files are supported. VideoStreams can't draw videos, see love.graphics.newVideo for that.

love.video.newVideoStream(filename)

| name | type | description |
| --- | --- | --- |
| filename | string | The file path to the Ogg Theora video file. |

| name | type | description |
| --- | --- | --- |
| videostream | VideoStream | A new VideoStream. |

love.video.newVideoStream(file)

| name | type | description |
| --- | --- | --- |
| file | File | The File object containing the Ogg Theora video. |

| name | type | description |
| --- | --- | --- |
| videostream | VideoStream | A new VideoStream. |


love.visible

Callback function triggered when window is minimized/hidden or unminimized by the user.

love.visible(visible)

| name | type | description |
| --- | --- | --- |
| visible | boolean | True if the window is visible, false if it isn't. |


love.wheelmoved

Callback function triggered when the mouse wheel is moved.

love.wheelmoved(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | Amount of horizontal mouse wheel movement. Positive values indicate movement to the right. |
| y | number | Amount of vertical mouse wheel movement. Positive values indicate upward movement. |


love.window.close

Closes the window. It can be reopened with love.window.setMode.

love.window.close()


love.window.fromPixels

Converts a number from pixels to density-independent units.

The pixel density inside the window might be greater (or smaller) than the 'size' of the window. For example on a retina screen in Mac OS X with the highdpi window flag enabled, the window may take up the same physical size as an 800x600 window, but the area inside the window uses 1600x1200 pixels. love.window.fromPixels(1600) would return 800 in that case.

This function converts coordinates from pixels to the size users are expecting them to display at onscreen. love.window.toPixels does the opposite. The highdpi window flag must be enabled to use the full pixel density of a Retina screen on Mac OS X and iOS. The flag currently does nothing on Windows and Linux, and on Android it is effectively always enabled.

Most LÖVE functions return values and expect arguments in terms of pixels rather than density-independent units.

love.window.fromPixels(pixelvalue)

| name | type | description |
| --- | --- | --- |
| pixelvalue | number | A number in pixels to convert to density-independent units. |

| name | type | description |
| --- | --- | --- |
| value | number | The converted number, in density-independent units. |

love.window.fromPixels(px, py)

| name | type | description |
| --- | --- | --- |
| px | number | The x-axis value of a coordinate in pixels. |
| py | number | The y-axis value of a coordinate in pixels. |

| name | type | description |
| --- | --- | --- |
| x | number | The converted x-axis value of the coordinate, in density-independent units. |
| y | number | The converted y-axis value of the coordinate, in density-independent units. |


love.window.getDPIScale

Gets the DPI scale factor associated with the window.

The pixel density inside the window might be greater (or smaller) than the 'size' of the window. For example on a retina screen in Mac OS X with the highdpi window flag enabled, the window may take up the same physical size as an 800x600 window, but the area inside the window uses 1600x1200 pixels. love.window.getDPIScale() would return 2.0 in that case.

The love.window.fromPixels and love.window.toPixels functions can also be used to convert between units.

The highdpi window flag must be enabled to use the full pixel density of a Retina screen on Mac OS X and iOS. The flag currently does nothing on Windows and Linux, and on Android it is effectively always enabled.

love.window.getDPIScale()

| name | type | description |
| --- | --- | --- |
| scale | number | The pixel scale factor associated with the window. |


love.window.getDesktopDimensions

Gets the width and height of the desktop.

love.window.getDesktopDimensions(displayindex)

| name | type | description |
| --- | --- | --- |
| displayindex | number | The index of the display, if multiple monitors are available. |

| name | type | description |
| --- | --- | --- |
| width | number | The width of the desktop. |
| height | number | The height of the desktop. |


love.window.getDisplayCount

Gets the number of connected monitors.

love.window.getDisplayCount()

| name | type | description |
| --- | --- | --- |
| count | number | The number of currently connected displays. |


love.window.getDisplayName

Gets the name of a display.

love.window.getDisplayName(displayindex)

| name | type | description |
| --- | --- | --- |
| displayindex | number | The index of the display to get the name of. |

| name | type | description |
| --- | --- | --- |
| name | string | The name of the specified display. |


love.window.getDisplayOrientation

Gets current device display orientation.

love.window.getDisplayOrientation(displayindex)

| name | type | description |
| --- | --- | --- |
| displayindex | number | Display index to get its display orientation, or nil for default display index. |

| name | type | description |
| --- | --- | --- |
| orientation | DisplayOrientation | Current device display orientation. |


love.window.getFullscreen

Gets whether the window is fullscreen.

love.window.getFullscreen()

| name | type | description |
| --- | --- | --- |
| fullscreen | boolean | True if the window is fullscreen, false otherwise. |
| fstype | FullscreenType | The type of fullscreen mode used. |


love.window.getFullscreenModes

Gets a list of supported fullscreen modes.

love.window.getFullscreenModes(displayindex)

| name | type | description |
| --- | --- | --- |
| displayindex | number | The index of the display, if multiple monitors are available. |

| name | type | description |
| --- | --- | --- |
| modes | table | A table of width/height pairs. (Note that this may not be in order.) |


love.window.getIcon

Gets the window icon.

love.window.getIcon()

| name | type | description |
| --- | --- | --- |
| imagedata | ImageData | The window icon imagedata, or nil if no icon has been set with love.window.setIcon. |


love.window.getMode

Gets the display mode and properties of the window.

love.window.getMode()

| name | type | description |
| --- | --- | --- |
| width | number | Window width. |
| height | number | Window height. |
| flags | table | Table with the window properties: |


love.window.getPosition

Gets the position of the window on the screen.

The window position is in the coordinate space of the display it is currently in.

love.window.getPosition()

| name | type | description |
| --- | --- | --- |
| x | number | The x-coordinate of the window's position. |
| y | number | The y-coordinate of the window's position. |
| displayindex | number | The index of the display that the window is in. |


love.window.getSafeArea

Gets area inside the window which is known to be unobstructed by a system title bar, the iPhone X notch, etc. Useful for making sure UI elements can be seen by the user.

love.window.getSafeArea()

| name | type | description |
| --- | --- | --- |
| x | number | Starting position of safe area (x-axis). |
| y | number | Starting position of safe area (y-axis). |
| w | number | Width of safe area. |
| h | number | Height of safe area. |


love.window.getTitle

Gets the window title.

love.window.getTitle()

| name | type | description |
| --- | --- | --- |
| title | string | The current window title. |


love.window.getVSync

Gets current vertical synchronization (vsync).

love.window.getVSync()

| name | type | description |
| --- | --- | --- |
| vsync | number | Current vsync status. 1 if enabled, 0 if disabled, and -1 for adaptive vsync. |


love.window.hasFocus

Checks if the game window has keyboard focus.

love.window.hasFocus()

| name | type | description |
| --- | --- | --- |
| focus | boolean | True if the window has the focus or false if not. |


love.window.hasMouseFocus

Checks if the game window has mouse focus.

love.window.hasMouseFocus()

| name | type | description |
| --- | --- | --- |
| focus | boolean | True if the window has mouse focus or false if not. |


love.window.isDisplaySleepEnabled

Gets whether the display is allowed to sleep while the program is running.

Display sleep is disabled by default. Some types of input (e.g. joystick button presses) might not prevent the display from sleeping, if display sleep is allowed.

love.window.isDisplaySleepEnabled()

| name | type | description |
| --- | --- | --- |
| enabled | boolean | True if system display sleep is enabled / allowed, false otherwise. |


love.window.isMaximized

Gets whether the Window is currently maximized.

The window can be maximized if it is not fullscreen and is resizable, and either the user has pressed the window's Maximize button or love.window.maximize has been called.

love.window.isMaximized()

| name | type | description |
| --- | --- | --- |
| maximized | boolean | True if the window is currently maximized in windowed mode, false otherwise. |


love.window.isMinimized

Gets whether the Window is currently minimized.

love.window.isMinimized()

| name | type | description |
| --- | --- | --- |
| minimized | boolean | True if the window is currently minimized, false otherwise. |


love.window.isOpen

Checks if the window is open.

love.window.isOpen()

| name | type | description |
| --- | --- | --- |
| open | boolean | True if the window is open, false otherwise. |


love.window.isVisible

Checks if the game window is visible.

The window is considered visible if it's not minimized and the program isn't hidden.

love.window.isVisible()

| name | type | description |
| --- | --- | --- |
| visible | boolean | True if the window is visible or false if not. |


love.window.maximize

Makes the window as large as possible.

This function has no effect if the window isn't resizable, since it essentially programmatically presses the window's 'maximize' button.

love.window.maximize()


love.window.minimize

Minimizes the window to the system's task bar / dock.

love.window.minimize()


love.window.requestAttention

Causes the window to request the attention of the user if it is not in the foreground.

In Windows the taskbar icon will flash, and in OS X the dock icon will bounce.

love.window.requestAttention(continuous)

| name | type | description |
| --- | --- | --- |
| continuous | boolean | Whether to continuously request attention until the window becomes active, or to do it only once. |


love.window.restore

Restores the size and position of the window if it was minimized or maximized.

love.window.restore()


love.window.setDisplaySleepEnabled

Sets whether the display is allowed to sleep while the program is running.

Display sleep is disabled by default. Some types of input (e.g. joystick button presses) might not prevent the display from sleeping, if display sleep is allowed.

love.window.setDisplaySleepEnabled(enable)

| name | type | description |
| --- | --- | --- |
| enable | boolean | True to enable system display sleep, false to disable it. |


love.window.setFullscreen

Enters or exits fullscreen. The display to use when entering fullscreen is chosen based on which display the window is currently in, if multiple monitors are connected.

love.window.setFullscreen(fullscreen)

| name | type | description |
| --- | --- | --- |
| fullscreen | boolean | Whether to enter or exit fullscreen mode. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if an attempt to enter fullscreen was successful, false otherwise. |

love.window.setFullscreen(fullscreen, fstype)

| name | type | description |
| --- | --- | --- |
| fullscreen | boolean | Whether to enter or exit fullscreen mode. |
| fstype | FullscreenType | The type of fullscreen mode to use. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if an attempt to enter fullscreen was successful, false otherwise. |


love.window.setIcon

Sets the window icon until the game is quit. Not all operating systems support very large icon images.

love.window.setIcon(imagedata)

| name | type | description |
| --- | --- | --- |
| imagedata | ImageData | The window icon image. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the icon has been set successfully. |


love.window.setMode

Sets the display mode and properties of the window.

If width or height is 0, setMode will use the width and height of the desktop.

Changing the display mode may have side effects: for example, canvases will be cleared and values sent to shaders with canvases beforehand or re-draw to them afterward if you need to.

love.window.setMode(width, height, flags)

| name | type | description |
| --- | --- | --- |
| width | number | Display width. |
| height | number | Display height. |
| flags | table | The flags table with the options: |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if successful, false otherwise. |


love.window.setPosition

Sets the position of the window on the screen.

The window position is in the coordinate space of the specified display.

love.window.setPosition(x, y, displayindex)

| name | type | description |
| --- | --- | --- |
| x | number | The x-coordinate of the window's position. |
| y | number | The y-coordinate of the window's position. |
| displayindex | number | The index of the display that the new window position is relative to. |


love.window.setTitle

Sets the window title.

love.window.setTitle(title)

| name | type | description |
| --- | --- | --- |
| title | string | The new window title. |


love.window.setVSync

Sets vertical synchronization mode.

love.window.setVSync(vsync)

| name | type | description |
| --- | --- | --- |
| vsync | number | VSync number: 1 to enable, 0 to disable, and -1 for adaptive vsync. |


love.window.showMessageBox

Displays a message box dialog above the love window. The message box contains a title, optional text, and buttons.

love.window.showMessageBox(title, message, type, attachtowindow)

| name | type | description |
| --- | --- | --- |
| title | string | The title of the message box. |
| message | string | The text inside the message box. |
| type | MessageBoxType | The type of the message box. |
| attachtowindow | boolean | Whether the message box should be attached to the love window or free-floating. |

| name | type | description |
| --- | --- | --- |
| success | boolean | Whether the message box was successfully displayed. |

love.window.showMessageBox(title, message, buttonlist, type, attachtowindow)

| name | type | description |
| --- | --- | --- |
| title | string | The title of the message box. |
| message | string | The text inside the message box. |
| buttonlist | table | A table containing a list of button names to show. The table can also contain the fields enterbutton and escapebutton, which should be the index of the default button to use when the user presses 'enter' or 'escape', respectively. |
| type | MessageBoxType | The type of the message box. |
| attachtowindow | boolean | Whether the message box should be attached to the love window or free-floating. |

| name | type | description |
| --- | --- | --- |
| pressedbutton | number | The index of the button pressed by the user. May be 0 if the message box dialog was closed without pressing a button. |


love.window.toPixels

Converts a number from density-independent units to pixels.

The pixel density inside the window might be greater (or smaller) than the 'size' of the window. For example on a retina screen in Mac OS X with the highdpi window flag enabled, the window may take up the same physical size as an 800x600 window, but the area inside the window uses 1600x1200 pixels. love.window.toPixels(800) would return 1600 in that case.

This is used to convert coordinates from the size users are expecting them to display at onscreen to pixels. love.window.fromPixels does the opposite. The highdpi window flag must be enabled to use the full pixel density of a Retina screen on Mac OS X and iOS. The flag currently does nothing on Windows and Linux, and on Android it is effectively always enabled.

Most LÖVE functions return values and expect arguments in terms of pixels rather than density-independent units.

love.window.toPixels(value)

| name | type | description |
| --- | --- | --- |
| value | number | A number in density-independent units to convert to pixels. |

| name | type | description |
| --- | --- | --- |
| pixelvalue | number | The converted number, in pixels. |

love.window.toPixels(x, y)

| name | type | description |
| --- | --- | --- |
| x | number | The x-axis value of a coordinate in density-independent units to convert to pixels. |
| y | number | The y-axis value of a coordinate in density-independent units to convert to pixels. |

| name | type | description |
| --- | --- | --- |
| px | number | The converted x-axis value of the coordinate, in pixels. |
| py | number | The converted y-axis value of the coordinate, in pixels. |


love.window.updateMode

Sets the display mode and properties of the window, without modifying unspecified properties.

If width or height is 0, updateMode will use the width and height of the desktop.

Changing the display mode may have side effects: for example, canvases will be cleared. Make sure to save the contents of canvases beforehand or re-draw to them afterward if you need to.

love.window.updateMode(width, height, settings)

| name | type | description |
| --- | --- | --- |
| width | number | Window width. |
| height | number | Window height. |
| settings | table | The settings table with the following optional fields. Any field not filled in will use the current value that would be returned by love.window.getMode. |

| name | type | description |
| --- | --- | --- |
| success | boolean | True if successful, false otherwise. |
